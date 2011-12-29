#!/bin/sh
java -jar antlr-3.4-complete-no-antlrv2.jar -language Python ./output/PLSQL3.g \
&& sed -ie '/private bool is_sql/ s/private.*$/is_sql = False/; /!is_sql/ s/!is_sql/not is_sql/g; /||/ s/||/or/g; /this\./ s/this\./self./g; /Text\.ToUpper/ s/\.Text\.ToUpper/.text.upper/g' output/PLSQL3Parser.py
