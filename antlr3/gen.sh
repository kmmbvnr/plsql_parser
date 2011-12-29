#!/bin/sh
DIR=$(dirname $0)
JAR=$DIR/lib/java/antlr-3.4-complete-no-antlrv2.jar
mkdir -p $DIR/classes
java -jar ${JAR} -language Java $DIR/PLSQL3.g \
&& sed -ie '/private bool is_sql/ s/bool /boolean /; /Text\.ToUpper/ s/\.Text\.ToUpper() == \("[^"]*"\)/.getText().equalsIgnoreCase(\1)/g; /Text\.toUpper/ s/\.Text\.ToUpper/.getText().toUpperCase()/g; /this\.input/ s/(this\.input)/input/g' $DIR/PLSQL3Parser.java \
&& javac -cp $JAR -d $DIR/classes $DIR/PLSQL3*.java
java -jar ${JAR} -language Python $DIR/PLSQL3.g \
&& sed -ie '/private bool is_sql/ s/private.*$/is_sql = False/; /!is_sql/ s/!is_sql/not is_sql/g; /||/ s/||/or/g; /this\./ s/this\./self./g; /Text\.ToUpper/ s/\.Text\.ToUpper/.text.upper/g' $DIR/PLSQL3Parser.py
