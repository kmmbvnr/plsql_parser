#!/bin/sh
DIR=$(dirname $0)/..
time cat ~/projects/unosoft/unora/unovk/test/elj_bruno.sql \
| PYTHONPATH=${DIR}/lib/python:$PYTHONPATH python ${DIR}/PLSQL3Parser.py --rule=create_package --encoding=iso8859_2
