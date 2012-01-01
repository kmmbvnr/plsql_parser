#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyparsing import *
import re
import zlib
import requests
from xml.sax.saxutils import unescape as html_unescape
import logging
LOG = logging.getLogger(__name__)

r_img_text = re.compile('href="(img_text/[^"]+\\.html?)"')
r_pre = re.compile('<pre[^>]*>(.*?)</pre>', re.S)
r_word = re.compile('[a-z0-9_]+')


def read_links(url, known={}, strict=True):
    base_url = url.rsplit('/', 1)[0]
    visited = set()
    unknown = set()
    met = set()
    urls = [url]
    while urls:
        url = urls.pop()
        try:
            links = list(_read_links(url, known=known, unknown=unknown, strict=strict))
        except AssertionError:
            LOG.warn('no luck with %r', url)
        else:
            for tup in links:
                if not tup[0] in met:
                    yield tup
                    met.add(tup[0])
            unknown -= set(known)
            if unknown:
                urls.extend(x for x in (base_url + '/' + key + '.htm'
                                        for key in unknown)
                            if not x in visited)
        finally:
            visited.add(url)
    LOG.info('UNKNOWN: %s', unknown)


def _read_links(url, known={}, unknown=set(), strict=True):
    LOG.info('reading links from %r', url)
    met = set()
    content = get_page(url, cache_nexists=not strict)
    if not strict and not content:
        return
    base_url = url.rsplit('/', 1)[0]
    for m in r_img_text.finditer(content):
        name = m.group(1)
        if name in met:
            continue
        else:
            met.add(name)
        tup = read_ebnf(base_url + '/' + name, strict=strict)
        if not tup:
            continue
        yield tup
        known[tup[0]] = tup[1]
        for m in r_word.finditer(tup[1]):
            word = m.group(0)
            if not word in known:
                unknown.add(word)


def read_ebnf(url, strict=True):
    LOG.debug('reading ebnf from %r', url)
    content = get_page(url, cache_nexists=not strict)
    if strict or content:
        m = r_pre.search(content)
        assert m, (content, url)
        return (url.rsplit('/', 1)[-1].rsplit('.', 1)[0],
                html_unescape(r_pre.search(content).group(1)))
    else:
        return None


_get_config = {'keep_alive': True, 'pool_maxsize': 100,
               'pool_connections': 10}

def get_page(url, cache_nexists=True):
    if not url in _cache:
        req = requests.get(url, prefetch=True, config=_get_config)
        if cache_nexists and not req.ok:
            _cache[url] = None
        else:
            assert req.ok
        _cache[url] = req.content
    return _cache[url]


class PageCache(object):
    def __init__(self, db_name='/tmp/cache.sqlite', compress_threshold=1024):
        self.compress_threshold = compress_threshold
        import sqlite3
        conn = sqlite3.connect(db_name)
        self.cu = conn.cursor()
        self.cu.execute('CREATE TABLE IF NOT EXISTS T_page_cache '
               '(url TEXT, text TEXT, compressed BLOB)')

    def __getitem__(self, key):
        self.cu.execute('SELECT text, compressed FROM T_page_cache '
                        'WHERE url = ?', [key])
        row = self.cu.next()
        return (None if not any(row)
                else (row[0] or self.decompress(row[1])))

    def __setitem__(self, key, value):
        self.cu.execute('REPLACE INTO T_page_cache (url, text, compressed) '
                        'VALUES (?, ?, ?)', [key] + list(self.compress(value)))
        self.cu.connection.commit()

    def __contains__(self, key):
        self.cu.execute('SELECT COUNT(0) FROM T_page_cache '
                        'WHERE url = ? LIMIT 1', [key])
        return self.cu.next()[0] > 0

    def get(self, key, default=None):
        return self[key] if key in self else default

    def compress(self, data):
        return ((None, buffer(zlib.compress(data, 2)))
                if data and len(data) > self.compress_threshold
                else (data, None))

    def decompress(self, data):
        return zlib.decompress(data)


_cache = PageCache()


def parse_ebnf(ebnf):

    table = {'label': Word(alphas, alphanums + '_#'),
             #'<<': Suppress('<<'), '>>': Suppress('>>'),
             'EOS': Suppress(';')}
    from ebnf_parser import parse as ebnf_parser
    ebnf = '''
plsql_block = [ label ] - [ DECLARE declare_section ] body;'''
    print ebnf_parser(ebnf, table)


if '__main__' == __name__:
    logging.basicConfig(level=logging.DEBUG)
    import sys
    urls = (sys.argv[1:] if len(sys.argv) > 1
           else [('http://docs.oracle.com/cd/E11882_01/appdev.112/e25519/'
                  + x + '.htm') for x in ('create_package', 'create_package_body',
                                          'block')])

    known = {'high_value': None, #'commit_statement': 'COMMIT;',
             #'rollback_statement': 'ROLLBACK;',
             'character_set': None, 'scale': "'0'..'9'"}
    ebnf = '\n'.join(
            '\n'.join(x[0] + ' = ' + x[1].rstrip().replace('<<',
                                                           '"<<"').replace('>>',
                       '">>"').replace(';', ' EOS') + ';'
               for x in read_links(url, known, strict=False))
            for url in urls)
    print ebnf
