# $ANTLR 3.4 /home/gthomas/projects/plsql/PLSQL3.g 2011-12-28 21:45:42

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__50=50
T__51=51
T__52=52
T__53=53
T__54=54
T__55=55
T__56=56
T__57=57
T__58=58
T__59=59
T__60=60
T__61=61
T__62=62
T__63=63
T__64=64
T__65=65
T__66=66
T__67=67
T__68=68
T__69=69
T__70=70
T__71=71
T__72=72
T__73=73
T__74=74
T__75=75
T__76=76
T__77=77
T__78=78
T__79=79
T__80=80
T__81=81
T__82=82
T__83=83
T__84=84
T__85=85
T__86=86
T__87=87
T__88=88
T__89=89
T__90=90
T__91=91
T__92=92
T__93=93
T__94=94
T__95=95
T__96=96
T__97=97
T__98=98
T__99=99
T__100=100
T__101=101
T__102=102
T__103=103
T__104=104
T__105=105
T__106=106
T__107=107
T__108=108
T__109=109
T__110=110
T__111=111
T__112=112
T__113=113
T__114=114
T__115=115
T__116=116
T__117=117
T__118=118
T__119=119
T__120=120
T__121=121
T__122=122
T__123=123
T__124=124
T__125=125
T__126=126
T__127=127
T__128=128
T__129=129
T__130=130
T__131=131
T__132=132
T__133=133
T__134=134
T__135=135
T__136=136
T__137=137
T__138=138
T__139=139
T__140=140
T__141=141
T__142=142
T__143=143
T__144=144
T__145=145
T__146=146
T__147=147
T__148=148
T__149=149
T__150=150
T__151=151
T__152=152
T__153=153
T__154=154
T__155=155
T__156=156
T__157=157
T__158=158
T__159=159
T__160=160
T__161=161
T__162=162
T__163=163
T__164=164
T__165=165
T__166=166
T__167=167
ARROW=4
ASSIGN=5
ASTERISK=6
AT_SIGN=7
BULK_ROWCOUNT_ATTR=8
CHARSET_ATTR=9
COLON=10
COMMA=11
DIVIDE=12
DOT=13
DOUBLEDOT=14
DOUBLEQUOTED_STRING=15
DOUBLEVERTBAR=16
EQ=17
EXPONENT=18
FOUND_ATTR=19
GEQ=20
GTH=21
ID=22
ISOPEN_ATTR=23
LBRACK=24
LEQ=25
LLABEL=26
LPAREN=27
LTH=28
MINUS=29
ML_COMMENT=30
N=31
NOTFOUND_ATTR=32
NOT_EQ=33
NUMBER=34
PERCENTAGE=35
PLUS=36
POINT=37
QUOTE=38
QUOTED_STRING=39
RBRACK=40
RLABEL=41
ROWCOUNT_ATTR=42
ROWTYPE_ATTR=43
RPAREN=44
SEMI=45
SL_COMMENT=46
TYPE_ATTR=47
VERTBAR=48
WS=49


class PLSQL3Lexer(Lexer):

    grammarFileName = "/home/gthomas/projects/plsql/PLSQL3.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(PLSQL3Lexer, self).__init__(input, state)

        self.delegates = []

        self.dfa6 = self.DFA6(
            self, 6,
            eot = self.DFA6_eot,
            eof = self.DFA6_eof,
            min = self.DFA6_min,
            max = self.DFA6_max,
            accept = self.DFA6_accept,
            special = self.DFA6_special,
            transition = self.DFA6_transition
            )

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )






    # $ANTLR start "T__50"
    def mT__50(self, ):
        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:7:7: ( 'ALL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:7:9: 'ALL'
            pass 
            self.match("ALL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):
        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:8:7: ( 'AND' )
            # /home/gthomas/projects/plsql/PLSQL3.g:8:9: 'AND'
            pass 
            self.match("AND")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):
        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:9:7: ( 'ANY' )
            # /home/gthomas/projects/plsql/PLSQL3.g:9:9: 'ANY'
            pass 
            self.match("ANY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):
        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:10:7: ( 'AS' )
            # /home/gthomas/projects/plsql/PLSQL3.g:10:9: 'AS'
            pass 
            self.match("AS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):
        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:11:7: ( 'ASC' )
            # /home/gthomas/projects/plsql/PLSQL3.g:11:9: 'ASC'
            pass 
            self.match("ASC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):
        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:12:7: ( 'AT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:12:9: 'AT'
            pass 
            self.match("AT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):
        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:13:7: ( 'BEGIN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:13:9: 'BEGIN'
            pass 
            self.match("BEGIN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__56"



    # $ANTLR start "T__57"
    def mT__57(self, ):
        try:
            _type = T__57
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:14:7: ( 'BETWEEN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:14:9: 'BETWEEN'
            pass 
            self.match("BETWEEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__57"



    # $ANTLR start "T__58"
    def mT__58(self, ):
        try:
            _type = T__58
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:15:7: ( 'BFILE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:15:9: 'BFILE'
            pass 
            self.match("BFILE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__58"



    # $ANTLR start "T__59"
    def mT__59(self, ):
        try:
            _type = T__59
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:16:7: ( 'BINARY_DOUBLE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:16:9: 'BINARY_DOUBLE'
            pass 
            self.match("BINARY_DOUBLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__59"



    # $ANTLR start "T__60"
    def mT__60(self, ):
        try:
            _type = T__60
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:17:7: ( 'BINARY_FLOAT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:17:9: 'BINARY_FLOAT'
            pass 
            self.match("BINARY_FLOAT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__60"



    # $ANTLR start "T__61"
    def mT__61(self, ):
        try:
            _type = T__61
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:18:7: ( 'BINARY_INTEGER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:18:9: 'BINARY_INTEGER'
            pass 
            self.match("BINARY_INTEGER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__61"



    # $ANTLR start "T__62"
    def mT__62(self, ):
        try:
            _type = T__62
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:19:7: ( 'BLOB' )
            # /home/gthomas/projects/plsql/PLSQL3.g:19:9: 'BLOB'
            pass 
            self.match("BLOB")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__62"



    # $ANTLR start "T__63"
    def mT__63(self, ):
        try:
            _type = T__63
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:20:7: ( 'BOOLEAN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:20:9: 'BOOLEAN'
            pass 
            self.match("BOOLEAN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__63"



    # $ANTLR start "T__64"
    def mT__64(self, ):
        try:
            _type = T__64
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:21:7: ( 'BY' )
            # /home/gthomas/projects/plsql/PLSQL3.g:21:9: 'BY'
            pass 
            self.match("BY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__64"



    # $ANTLR start "T__65"
    def mT__65(self, ):
        try:
            _type = T__65
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:22:7: ( 'CASE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:22:9: 'CASE'
            pass 
            self.match("CASE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__65"



    # $ANTLR start "T__66"
    def mT__66(self, ):
        try:
            _type = T__66
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:23:7: ( 'CHAR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:23:9: 'CHAR'
            pass 
            self.match("CHAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__66"



    # $ANTLR start "T__67"
    def mT__67(self, ):
        try:
            _type = T__67
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:24:7: ( 'CHARACTER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:24:9: 'CHARACTER'
            pass 
            self.match("CHARACTER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__67"



    # $ANTLR start "T__68"
    def mT__68(self, ):
        try:
            _type = T__68
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:25:7: ( 'CLOB' )
            # /home/gthomas/projects/plsql/PLSQL3.g:25:9: 'CLOB'
            pass 
            self.match("CLOB")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__68"



    # $ANTLR start "T__69"
    def mT__69(self, ):
        try:
            _type = T__69
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:26:7: ( 'COMMENT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:26:9: 'COMMENT'
            pass 
            self.match("COMMENT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__69"



    # $ANTLR start "T__70"
    def mT__70(self, ):
        try:
            _type = T__70
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:27:7: ( 'COMMIT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:27:9: 'COMMIT'
            pass 
            self.match("COMMIT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__70"



    # $ANTLR start "T__71"
    def mT__71(self, ):
        try:
            _type = T__71
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:28:7: ( 'CONNECT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:28:9: 'CONNECT'
            pass 
            self.match("CONNECT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__71"



    # $ANTLR start "T__72"
    def mT__72(self, ):
        try:
            _type = T__72
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:29:7: ( 'CONSTANT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:29:9: 'CONSTANT'
            pass 
            self.match("CONSTANT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__72"



    # $ANTLR start "T__73"
    def mT__73(self, ):
        try:
            _type = T__73
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:30:7: ( 'CREATE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:30:9: 'CREATE'
            pass 
            self.match("CREATE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__73"



    # $ANTLR start "T__74"
    def mT__74(self, ):
        try:
            _type = T__74
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:31:7: ( 'DATE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:31:9: 'DATE'
            pass 
            self.match("DATE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__74"



    # $ANTLR start "T__75"
    def mT__75(self, ):
        try:
            _type = T__75
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:32:7: ( 'DEC' )
            # /home/gthomas/projects/plsql/PLSQL3.g:32:9: 'DEC'
            pass 
            self.match("DEC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__75"



    # $ANTLR start "T__76"
    def mT__76(self, ):
        try:
            _type = T__76
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:33:7: ( 'DECIMAL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:33:9: 'DECIMAL'
            pass 
            self.match("DECIMAL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__76"



    # $ANTLR start "T__77"
    def mT__77(self, ):
        try:
            _type = T__77
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:34:7: ( 'DECLARE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:34:9: 'DECLARE'
            pass 
            self.match("DECLARE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__77"



    # $ANTLR start "T__78"
    def mT__78(self, ):
        try:
            _type = T__78
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:35:7: ( 'DEFAULT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:35:9: 'DEFAULT'
            pass 
            self.match("DEFAULT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__78"



    # $ANTLR start "T__79"
    def mT__79(self, ):
        try:
            _type = T__79
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:36:7: ( 'DELETE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:36:9: 'DELETE'
            pass 
            self.match("DELETE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__79"



    # $ANTLR start "T__80"
    def mT__80(self, ):
        try:
            _type = T__80
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:37:7: ( 'DESC' )
            # /home/gthomas/projects/plsql/PLSQL3.g:37:9: 'DESC'
            pass 
            self.match("DESC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__80"



    # $ANTLR start "T__81"
    def mT__81(self, ):
        try:
            _type = T__81
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:38:7: ( 'DISTINCT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:38:9: 'DISTINCT'
            pass 
            self.match("DISTINCT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__81"



    # $ANTLR start "T__82"
    def mT__82(self, ):
        try:
            _type = T__82
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:39:7: ( 'DOUBLE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:39:9: 'DOUBLE'
            pass 
            self.match("DOUBLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__82"



    # $ANTLR start "T__83"
    def mT__83(self, ):
        try:
            _type = T__83
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:40:7: ( 'ELSE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:40:9: 'ELSE'
            pass 
            self.match("ELSE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__83"



    # $ANTLR start "T__84"
    def mT__84(self, ):
        try:
            _type = T__84
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:41:7: ( 'ELSIF' )
            # /home/gthomas/projects/plsql/PLSQL3.g:41:9: 'ELSIF'
            pass 
            self.match("ELSIF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__84"



    # $ANTLR start "T__85"
    def mT__85(self, ):
        try:
            _type = T__85
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:42:7: ( 'END' )
            # /home/gthomas/projects/plsql/PLSQL3.g:42:9: 'END'
            pass 
            self.match("END")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__85"



    # $ANTLR start "T__86"
    def mT__86(self, ):
        try:
            _type = T__86
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:43:7: ( 'EXCEPTION' )
            # /home/gthomas/projects/plsql/PLSQL3.g:43:9: 'EXCEPTION'
            pass 
            self.match("EXCEPTION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__86"



    # $ANTLR start "T__87"
    def mT__87(self, ):
        try:
            _type = T__87
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:44:7: ( 'EXCLUSIVE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:44:9: 'EXCLUSIVE'
            pass 
            self.match("EXCLUSIVE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__87"



    # $ANTLR start "T__88"
    def mT__88(self, ):
        try:
            _type = T__88
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:45:7: ( 'EXISTS' )
            # /home/gthomas/projects/plsql/PLSQL3.g:45:9: 'EXISTS'
            pass 
            self.match("EXISTS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__88"



    # $ANTLR start "T__89"
    def mT__89(self, ):
        try:
            _type = T__89
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:46:7: ( 'FALSE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:46:9: 'FALSE'
            pass 
            self.match("FALSE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__89"



    # $ANTLR start "T__90"
    def mT__90(self, ):
        try:
            _type = T__90
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:47:7: ( 'FETCH' )
            # /home/gthomas/projects/plsql/PLSQL3.g:47:9: 'FETCH'
            pass 
            self.match("FETCH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__90"



    # $ANTLR start "T__91"
    def mT__91(self, ):
        try:
            _type = T__91
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:48:7: ( 'FLOAT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:48:9: 'FLOAT'
            pass 
            self.match("FLOAT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__91"



    # $ANTLR start "T__92"
    def mT__92(self, ):
        try:
            _type = T__92
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:49:7: ( 'FOR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:49:9: 'FOR'
            pass 
            self.match("FOR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__92"



    # $ANTLR start "T__93"
    def mT__93(self, ):
        try:
            _type = T__93
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:50:7: ( 'FROM' )
            # /home/gthomas/projects/plsql/PLSQL3.g:50:9: 'FROM'
            pass 
            self.match("FROM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__93"



    # $ANTLR start "T__94"
    def mT__94(self, ):
        try:
            _type = T__94
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:51:7: ( 'FUNCTION' )
            # /home/gthomas/projects/plsql/PLSQL3.g:51:9: 'FUNCTION'
            pass 
            self.match("FUNCTION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__94"



    # $ANTLR start "T__95"
    def mT__95(self, ):
        try:
            _type = T__95
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:52:7: ( 'GOTO' )
            # /home/gthomas/projects/plsql/PLSQL3.g:52:9: 'GOTO'
            pass 
            self.match("GOTO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__95"



    # $ANTLR start "T__96"
    def mT__96(self, ):
        try:
            _type = T__96
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:53:7: ( 'GROUP' )
            # /home/gthomas/projects/plsql/PLSQL3.g:53:9: 'GROUP'
            pass 
            self.match("GROUP")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__96"



    # $ANTLR start "T__97"
    def mT__97(self, ):
        try:
            _type = T__97
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:54:7: ( 'HAVING' )
            # /home/gthomas/projects/plsql/PLSQL3.g:54:9: 'HAVING'
            pass 
            self.match("HAVING")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__97"



    # $ANTLR start "T__98"
    def mT__98(self, ):
        try:
            _type = T__98
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:55:7: ( 'IF' )
            # /home/gthomas/projects/plsql/PLSQL3.g:55:9: 'IF'
            pass 
            self.match("IF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__98"



    # $ANTLR start "T__99"
    def mT__99(self, ):
        try:
            _type = T__99
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:56:7: ( 'IN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:56:9: 'IN'
            pass 
            self.match("IN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__99"



    # $ANTLR start "T__100"
    def mT__100(self, ):
        try:
            _type = T__100
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:57:8: ( 'INDEX' )
            # /home/gthomas/projects/plsql/PLSQL3.g:57:10: 'INDEX'
            pass 
            self.match("INDEX")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__100"



    # $ANTLR start "T__101"
    def mT__101(self, ):
        try:
            _type = T__101
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:58:8: ( 'INSERT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:58:10: 'INSERT'
            pass 
            self.match("INSERT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__101"



    # $ANTLR start "T__102"
    def mT__102(self, ):
        try:
            _type = T__102
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:59:8: ( 'INT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:59:10: 'INT'
            pass 
            self.match("INT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__102"



    # $ANTLR start "T__103"
    def mT__103(self, ):
        try:
            _type = T__103
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:60:8: ( 'INTEGER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:60:10: 'INTEGER'
            pass 
            self.match("INTEGER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__103"



    # $ANTLR start "T__104"
    def mT__104(self, ):
        try:
            _type = T__104
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:61:8: ( 'INTERSECT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:61:10: 'INTERSECT'
            pass 
            self.match("INTERSECT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__104"



    # $ANTLR start "T__105"
    def mT__105(self, ):
        try:
            _type = T__105
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:62:8: ( 'INTO' )
            # /home/gthomas/projects/plsql/PLSQL3.g:62:10: 'INTO'
            pass 
            self.match("INTO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__105"



    # $ANTLR start "T__106"
    def mT__106(self, ):
        try:
            _type = T__106
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:63:8: ( 'IS' )
            # /home/gthomas/projects/plsql/PLSQL3.g:63:10: 'IS'
            pass 
            self.match("IS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__106"



    # $ANTLR start "T__107"
    def mT__107(self, ):
        try:
            _type = T__107
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:64:8: ( 'LIKE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:64:10: 'LIKE'
            pass 
            self.match("LIKE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__107"



    # $ANTLR start "T__108"
    def mT__108(self, ):
        try:
            _type = T__108
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:65:8: ( 'LOCK' )
            # /home/gthomas/projects/plsql/PLSQL3.g:65:10: 'LOCK'
            pass 
            self.match("LOCK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__108"



    # $ANTLR start "T__109"
    def mT__109(self, ):
        try:
            _type = T__109
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:66:8: ( 'LONG' )
            # /home/gthomas/projects/plsql/PLSQL3.g:66:10: 'LONG'
            pass 
            self.match("LONG")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__109"



    # $ANTLR start "T__110"
    def mT__110(self, ):
        try:
            _type = T__110
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:67:8: ( 'LOOP' )
            # /home/gthomas/projects/plsql/PLSQL3.g:67:10: 'LOOP'
            pass 
            self.match("LOOP")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__110"



    # $ANTLR start "T__111"
    def mT__111(self, ):
        try:
            _type = T__111
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:68:8: ( 'MINUS' )
            # /home/gthomas/projects/plsql/PLSQL3.g:68:10: 'MINUS'
            pass 
            self.match("MINUS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__111"



    # $ANTLR start "T__112"
    def mT__112(self, ):
        try:
            _type = T__112
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:69:8: ( 'MLSLABEL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:69:10: 'MLSLABEL'
            pass 
            self.match("MLSLABEL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__112"



    # $ANTLR start "T__113"
    def mT__113(self, ):
        try:
            _type = T__113
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:70:8: ( 'MODE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:70:10: 'MODE'
            pass 
            self.match("MODE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__113"



    # $ANTLR start "T__114"
    def mT__114(self, ):
        try:
            _type = T__114
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:71:8: ( 'NATIONAL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:71:10: 'NATIONAL'
            pass 
            self.match("NATIONAL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__114"



    # $ANTLR start "T__115"
    def mT__115(self, ):
        try:
            _type = T__115
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:72:8: ( 'NATURAL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:72:10: 'NATURAL'
            pass 
            self.match("NATURAL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__115"



    # $ANTLR start "T__116"
    def mT__116(self, ):
        try:
            _type = T__116
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:73:8: ( 'NCHAR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:73:10: 'NCHAR'
            pass 
            self.match("NCHAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__116"



    # $ANTLR start "T__117"
    def mT__117(self, ):
        try:
            _type = T__117
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:74:8: ( 'NCLOB' )
            # /home/gthomas/projects/plsql/PLSQL3.g:74:10: 'NCLOB'
            pass 
            self.match("NCLOB")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__117"



    # $ANTLR start "T__118"
    def mT__118(self, ):
        try:
            _type = T__118
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:75:8: ( 'NOT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:75:10: 'NOT'
            pass 
            self.match("NOT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__118"



    # $ANTLR start "T__119"
    def mT__119(self, ):
        try:
            _type = T__119
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:76:8: ( 'NOWAIT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:76:10: 'NOWAIT'
            pass 
            self.match("NOWAIT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__119"



    # $ANTLR start "T__120"
    def mT__120(self, ):
        try:
            _type = T__120
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:77:8: ( 'NULL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:77:10: 'NULL'
            pass 
            self.match("NULL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__120"



    # $ANTLR start "T__121"
    def mT__121(self, ):
        try:
            _type = T__121
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:78:8: ( 'NUMBER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:78:10: 'NUMBER'
            pass 
            self.match("NUMBER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__121"



    # $ANTLR start "T__122"
    def mT__122(self, ):
        try:
            _type = T__122
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:79:8: ( 'NUMERIC' )
            # /home/gthomas/projects/plsql/PLSQL3.g:79:10: 'NUMERIC'
            pass 
            self.match("NUMERIC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__122"



    # $ANTLR start "T__123"
    def mT__123(self, ):
        try:
            _type = T__123
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:80:8: ( 'NVARCHAR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:80:10: 'NVARCHAR'
            pass 
            self.match("NVARCHAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__123"



    # $ANTLR start "T__124"
    def mT__124(self, ):
        try:
            _type = T__124
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:81:8: ( 'NVARCHAR2' )
            # /home/gthomas/projects/plsql/PLSQL3.g:81:10: 'NVARCHAR2'
            pass 
            self.match("NVARCHAR2")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__124"



    # $ANTLR start "T__125"
    def mT__125(self, ):
        try:
            _type = T__125
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:82:8: ( 'OF' )
            # /home/gthomas/projects/plsql/PLSQL3.g:82:10: 'OF'
            pass 
            self.match("OF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__125"



    # $ANTLR start "T__126"
    def mT__126(self, ):
        try:
            _type = T__126
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:83:8: ( 'ON' )
            # /home/gthomas/projects/plsql/PLSQL3.g:83:10: 'ON'
            pass 
            self.match("ON")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__126"



    # $ANTLR start "T__127"
    def mT__127(self, ):
        try:
            _type = T__127
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:84:8: ( 'OR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:84:10: 'OR'
            pass 
            self.match("OR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__127"



    # $ANTLR start "T__128"
    def mT__128(self, ):
        try:
            _type = T__128
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:85:8: ( 'ORDER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:85:10: 'ORDER'
            pass 
            self.match("ORDER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__128"



    # $ANTLR start "T__129"
    def mT__129(self, ):
        try:
            _type = T__129
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:86:8: ( 'OUT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:86:10: 'OUT'
            pass 
            self.match("OUT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__129"



    # $ANTLR start "T__130"
    def mT__130(self, ):
        try:
            _type = T__130
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:87:8: ( 'PACKAGE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:87:10: 'PACKAGE'
            pass 
            self.match("PACKAGE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__130"



    # $ANTLR start "T__131"
    def mT__131(self, ):
        try:
            _type = T__131
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:88:8: ( 'PLS_INTEGER' )
            # /home/gthomas/projects/plsql/PLSQL3.g:88:10: 'PLS_INTEGER'
            pass 
            self.match("PLS_INTEGER")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__131"



    # $ANTLR start "T__132"
    def mT__132(self, ):
        try:
            _type = T__132
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:89:8: ( 'POSITIVE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:89:10: 'POSITIVE'
            pass 
            self.match("POSITIVE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__132"



    # $ANTLR start "T__133"
    def mT__133(self, ):
        try:
            _type = T__133
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:90:8: ( 'PRAGMA' )
            # /home/gthomas/projects/plsql/PLSQL3.g:90:10: 'PRAGMA'
            pass 
            self.match("PRAGMA")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__133"



    # $ANTLR start "T__134"
    def mT__134(self, ):
        try:
            _type = T__134
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:91:8: ( 'PRIOR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:91:10: 'PRIOR'
            pass 
            self.match("PRIOR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__134"



    # $ANTLR start "T__135"
    def mT__135(self, ):
        try:
            _type = T__135
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:92:8: ( 'PROCEDURE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:92:10: 'PROCEDURE'
            pass 
            self.match("PROCEDURE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__135"



    # $ANTLR start "T__136"
    def mT__136(self, ):
        try:
            _type = T__136
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:93:8: ( 'RAISE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:93:10: 'RAISE'
            pass 
            self.match("RAISE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__136"



    # $ANTLR start "T__137"
    def mT__137(self, ):
        try:
            _type = T__137
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:94:8: ( 'RAW' )
            # /home/gthomas/projects/plsql/PLSQL3.g:94:10: 'RAW'
            pass 
            self.match("RAW")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__137"



    # $ANTLR start "T__138"
    def mT__138(self, ):
        try:
            _type = T__138
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:95:8: ( 'REAL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:95:10: 'REAL'
            pass 
            self.match("REAL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__138"



    # $ANTLR start "T__139"
    def mT__139(self, ):
        try:
            _type = T__139
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:96:8: ( 'RECORD' )
            # /home/gthomas/projects/plsql/PLSQL3.g:96:10: 'RECORD'
            pass 
            self.match("RECORD")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__139"



    # $ANTLR start "T__140"
    def mT__140(self, ):
        try:
            _type = T__140
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:97:8: ( 'RETURN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:97:10: 'RETURN'
            pass 
            self.match("RETURN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__140"



    # $ANTLR start "T__141"
    def mT__141(self, ):
        try:
            _type = T__141
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:98:8: ( 'RETURNING' )
            # /home/gthomas/projects/plsql/PLSQL3.g:98:10: 'RETURNING'
            pass 
            self.match("RETURNING")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__141"



    # $ANTLR start "T__142"
    def mT__142(self, ):
        try:
            _type = T__142
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:99:8: ( 'ROLLBACK' )
            # /home/gthomas/projects/plsql/PLSQL3.g:99:10: 'ROLLBACK'
            pass 
            self.match("ROLLBACK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__142"



    # $ANTLR start "T__143"
    def mT__143(self, ):
        try:
            _type = T__143
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:100:8: ( 'ROW' )
            # /home/gthomas/projects/plsql/PLSQL3.g:100:10: 'ROW'
            pass 
            self.match("ROW")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__143"



    # $ANTLR start "T__144"
    def mT__144(self, ):
        try:
            _type = T__144
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:101:8: ( 'ROWID' )
            # /home/gthomas/projects/plsql/PLSQL3.g:101:10: 'ROWID'
            pass 
            self.match("ROWID")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__144"



    # $ANTLR start "T__145"
    def mT__145(self, ):
        try:
            _type = T__145
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:102:8: ( 'ROWS' )
            # /home/gthomas/projects/plsql/PLSQL3.g:102:10: 'ROWS'
            pass 
            self.match("ROWS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__145"



    # $ANTLR start "T__146"
    def mT__146(self, ):
        try:
            _type = T__146
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:103:8: ( 'SAVEPOINT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:103:10: 'SAVEPOINT'
            pass 
            self.match("SAVEPOINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__146"



    # $ANTLR start "T__147"
    def mT__147(self, ):
        try:
            _type = T__147
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:104:8: ( 'SELECT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:104:10: 'SELECT'
            pass 
            self.match("SELECT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__147"



    # $ANTLR start "T__148"
    def mT__148(self, ):
        try:
            _type = T__148
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:105:8: ( 'SET' )
            # /home/gthomas/projects/plsql/PLSQL3.g:105:10: 'SET'
            pass 
            self.match("SET")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__148"



    # $ANTLR start "T__149"
    def mT__149(self, ):
        try:
            _type = T__149
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:106:8: ( 'SHARE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:106:10: 'SHARE'
            pass 
            self.match("SHARE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__149"



    # $ANTLR start "T__150"
    def mT__150(self, ):
        try:
            _type = T__150
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:107:8: ( 'SMALLINT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:107:10: 'SMALLINT'
            pass 
            self.match("SMALLINT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__150"



    # $ANTLR start "T__151"
    def mT__151(self, ):
        try:
            _type = T__151
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:108:8: ( 'SQL' )
            # /home/gthomas/projects/plsql/PLSQL3.g:108:10: 'SQL'
            pass 
            self.match("SQL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__151"



    # $ANTLR start "T__152"
    def mT__152(self, ):
        try:
            _type = T__152
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:109:8: ( 'START' )
            # /home/gthomas/projects/plsql/PLSQL3.g:109:10: 'START'
            pass 
            self.match("START")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__152"



    # $ANTLR start "T__153"
    def mT__153(self, ):
        try:
            _type = T__153
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:110:8: ( 'TABLE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:110:10: 'TABLE'
            pass 
            self.match("TABLE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__153"



    # $ANTLR start "T__154"
    def mT__154(self, ):
        try:
            _type = T__154
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:111:8: ( 'THEN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:111:10: 'THEN'
            pass 
            self.match("THEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__154"



    # $ANTLR start "T__155"
    def mT__155(self, ):
        try:
            _type = T__155
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:112:8: ( 'TO' )
            # /home/gthomas/projects/plsql/PLSQL3.g:112:10: 'TO'
            pass 
            self.match("TO")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__155"



    # $ANTLR start "T__156"
    def mT__156(self, ):
        try:
            _type = T__156
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:113:8: ( 'TRUE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:113:10: 'TRUE'
            pass 
            self.match("TRUE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__156"



    # $ANTLR start "T__157"
    def mT__157(self, ):
        try:
            _type = T__157
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:114:8: ( 'UNION' )
            # /home/gthomas/projects/plsql/PLSQL3.g:114:10: 'UNION'
            pass 
            self.match("UNION")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__157"



    # $ANTLR start "T__158"
    def mT__158(self, ):
        try:
            _type = T__158
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:115:8: ( 'UNIQUE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:115:10: 'UNIQUE'
            pass 
            self.match("UNIQUE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__158"



    # $ANTLR start "T__159"
    def mT__159(self, ):
        try:
            _type = T__159
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:116:8: ( 'UPDATE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:116:10: 'UPDATE'
            pass 
            self.match("UPDATE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__159"



    # $ANTLR start "T__160"
    def mT__160(self, ):
        try:
            _type = T__160
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:117:8: ( 'UROWID' )
            # /home/gthomas/projects/plsql/PLSQL3.g:117:10: 'UROWID'
            pass 
            self.match("UROWID")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__160"



    # $ANTLR start "T__161"
    def mT__161(self, ):
        try:
            _type = T__161
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:118:8: ( 'VALUES' )
            # /home/gthomas/projects/plsql/PLSQL3.g:118:10: 'VALUES'
            pass 
            self.match("VALUES")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__161"



    # $ANTLR start "T__162"
    def mT__162(self, ):
        try:
            _type = T__162
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:119:8: ( 'VARCHAR' )
            # /home/gthomas/projects/plsql/PLSQL3.g:119:10: 'VARCHAR'
            pass 
            self.match("VARCHAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__162"



    # $ANTLR start "T__163"
    def mT__163(self, ):
        try:
            _type = T__163
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:120:8: ( 'VARCHAR2' )
            # /home/gthomas/projects/plsql/PLSQL3.g:120:10: 'VARCHAR2'
            pass 
            self.match("VARCHAR2")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__163"



    # $ANTLR start "T__164"
    def mT__164(self, ):
        try:
            _type = T__164
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:121:8: ( 'WHEN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:121:10: 'WHEN'
            pass 
            self.match("WHEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__164"



    # $ANTLR start "T__165"
    def mT__165(self, ):
        try:
            _type = T__165
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:122:8: ( 'WHERE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:122:10: 'WHERE'
            pass 
            self.match("WHERE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__165"



    # $ANTLR start "T__166"
    def mT__166(self, ):
        try:
            _type = T__166
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:123:8: ( 'WHILE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:123:10: 'WHILE'
            pass 
            self.match("WHILE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__166"



    # $ANTLR start "T__167"
    def mT__167(self, ):
        try:
            _type = T__167
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:124:8: ( 'WITH' )
            # /home/gthomas/projects/plsql/PLSQL3.g:124:10: 'WITH'
            pass 
            self.match("WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__167"



    # $ANTLR start "QUOTED_STRING"
    def mQUOTED_STRING(self, ):
        try:
            _type = QUOTED_STRING
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1457:2: ( ( 'n' )? '\\'' ( '\\'\\'' |~ ( '\\'' ) )* '\\'' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1457:4: ( 'n' )? '\\'' ( '\\'\\'' |~ ( '\\'' ) )* '\\''
            pass 
            # /home/gthomas/projects/plsql/PLSQL3.g:1457:4: ( 'n' )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 110) :
                alt1 = 1
            if alt1 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1457:6: 'n'
                pass 
                self.match(110)




            self.match(39)

            # /home/gthomas/projects/plsql/PLSQL3.g:1457:18: ( '\\'\\'' |~ ( '\\'' ) )*
            while True: #loop2
                alt2 = 3
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 39) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 39) :
                        alt2 = 1


                elif ((0 <= LA2_0 <= 38) or (40 <= LA2_0 <= 65535)) :
                    alt2 = 2


                if alt2 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:1457:20: '\\'\\''
                    pass 
                    self.match("''")



                elif alt2 == 2:
                    # /home/gthomas/projects/plsql/PLSQL3.g:1457:29: ~ ( '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop2


            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUOTED_STRING"



    # $ANTLR start "ID"
    def mID(self, ):
        try:
            _type = ID
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1460:5: ( 'A' .. 'Z' ( 'A' .. 'Z' | '0' .. '9' | '_' | '$' | '#' )* | DOUBLEQUOTED_STRING )
            alt4 = 2
            LA4_0 = self.input.LA(1)

            if ((65 <= LA4_0 <= 90)) :
                alt4 = 1
            elif (LA4_0 == 34) :
                alt4 = 2
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 4, 0, self.input)

                raise nvae


            if alt4 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1460:7: 'A' .. 'Z' ( 'A' .. 'Z' | '0' .. '9' | '_' | '$' | '#' )*
                pass 
                self.matchRange(65, 90)

                # /home/gthomas/projects/plsql/PLSQL3.g:1460:18: ( 'A' .. 'Z' | '0' .. '9' | '_' | '$' | '#' )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((35 <= LA3_0 <= 36) or (48 <= LA3_0 <= 57) or (65 <= LA3_0 <= 90) or LA3_0 == 95) :
                        alt3 = 1


                    if alt3 == 1:
                        # /home/gthomas/projects/plsql/PLSQL3.g:
                        pass 
                        if (35 <= self.input.LA(1) <= 36) or (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95:
                            self.input.consume()
                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop3



            elif alt4 == 2:
                # /home/gthomas/projects/plsql/PLSQL3.g:1461:7: DOUBLEQUOTED_STRING
                pass 
                self.mDOUBLEQUOTED_STRING()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ID"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):
        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1464:2: ( ';' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1464:4: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "COLON"
    def mCOLON(self, ):
        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1467:2: ( ':' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1467:4: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COLON"



    # $ANTLR start "DOUBLEDOT"
    def mDOUBLEDOT(self, ):
        try:
            _type = DOUBLEDOT
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1470:2: ( POINT POINT )
            # /home/gthomas/projects/plsql/PLSQL3.g:1470:4: POINT POINT
            pass 
            self.mPOINT()


            self.mPOINT()




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOUBLEDOT"



    # $ANTLR start "DOT"
    def mDOT(self, ):
        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1473:2: ( POINT )
            # /home/gthomas/projects/plsql/PLSQL3.g:
            pass 
            if self.input.LA(1) == 46:
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOT"



    # $ANTLR start "POINT"
    def mPOINT(self, ):
        try:
            # /home/gthomas/projects/plsql/PLSQL3.g:1478:2: ( '.' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1478:4: '.'
            pass 
            self.match(46)




        finally:
            pass

    # $ANTLR end "POINT"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1480:2: ( ',' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1480:4: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            _type = EXPONENT
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1483:2: ( '**' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1483:4: '**'
            pass 
            self.match("**")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "ASTERISK"
    def mASTERISK(self, ):
        try:
            _type = ASTERISK
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1486:2: ( '*' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1486:4: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASTERISK"



    # $ANTLR start "AT_SIGN"
    def mAT_SIGN(self, ):
        try:
            _type = AT_SIGN
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1489:2: ( '@' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1489:4: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_SIGN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):
        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1492:2: ( ')' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1492:4: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):
        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1495:2: ( '(' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1495:4: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RBRACK"
    def mRBRACK(self, ):
        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1498:2: ( ']' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1498:4: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RBRACK"



    # $ANTLR start "LBRACK"
    def mLBRACK(self, ):
        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1501:2: ( '[' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1501:4: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LBRACK"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1504:2: ( '+' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1504:4: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):
        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1507:2: ( '-' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1507:4: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "DIVIDE"
    def mDIVIDE(self, ):
        try:
            _type = DIVIDE
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1510:2: ( '/' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1510:4: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DIVIDE"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1513:2: ( '=' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1513:4: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "PERCENTAGE"
    def mPERCENTAGE(self, ):
        try:
            _type = PERCENTAGE
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1516:2: ( '%' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1516:4: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PERCENTAGE"



    # $ANTLR start "LLABEL"
    def mLLABEL(self, ):
        try:
            _type = LLABEL
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1519:2: ( '<<' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1519:4: '<<'
            pass 
            self.match("<<")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LLABEL"



    # $ANTLR start "RLABEL"
    def mRLABEL(self, ):
        try:
            _type = RLABEL
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1522:2: ( '>>' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1522:4: '>>'
            pass 
            self.match(">>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RLABEL"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):
        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1525:2: ( ':=' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1525:4: ':='
            pass 
            self.match(":=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "ARROW"
    def mARROW(self, ):
        try:
            _type = ARROW
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1528:2: ( '=>' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1528:4: '=>'
            pass 
            self.match("=>")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW"



    # $ANTLR start "VERTBAR"
    def mVERTBAR(self, ):
        try:
            _type = VERTBAR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1531:2: ( '|' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1531:4: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VERTBAR"



    # $ANTLR start "DOUBLEVERTBAR"
    def mDOUBLEVERTBAR(self, ):
        try:
            _type = DOUBLEVERTBAR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1534:2: ( '||' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1534:4: '||'
            pass 
            self.match("||")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DOUBLEVERTBAR"



    # $ANTLR start "NOT_EQ"
    def mNOT_EQ(self, ):
        try:
            _type = NOT_EQ
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1537:2: ( '<>' | '!=' | '^=' )
            alt5 = 3
            LA5 = self.input.LA(1)
            if LA5 == 60:
                alt5 = 1
            elif LA5 == 33:
                alt5 = 2
            elif LA5 == 94:
                alt5 = 3
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae


            if alt5 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1537:4: '<>'
                pass 
                self.match("<>")



            elif alt5 == 2:
                # /home/gthomas/projects/plsql/PLSQL3.g:1537:11: '!='
                pass 
                self.match("!=")



            elif alt5 == 3:
                # /home/gthomas/projects/plsql/PLSQL3.g:1537:18: '^='
                pass 
                self.match("^=")



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOT_EQ"



    # $ANTLR start "LTH"
    def mLTH(self, ):
        try:
            _type = LTH
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1540:2: ( '<' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1540:4: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LTH"



    # $ANTLR start "LEQ"
    def mLEQ(self, ):
        try:
            _type = LEQ
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1543:2: ( '<=' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1543:4: '<='
            pass 
            self.match("<=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LEQ"



    # $ANTLR start "GTH"
    def mGTH(self, ):
        try:
            _type = GTH
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1546:2: ( '>' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1546:4: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GTH"



    # $ANTLR start "GEQ"
    def mGEQ(self, ):
        try:
            _type = GEQ
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1549:2: ( '>=' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1549:4: '>='
            pass 
            self.match(">=")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "GEQ"



    # $ANTLR start "NUMBER"
    def mNUMBER(self, ):
        try:
            _type = NUMBER
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1552:2: ( ( ( N POINT N )=> N POINT N | POINT N | N ) ( 'E' ( PLUS | MINUS )? N )? )
            # /home/gthomas/projects/plsql/PLSQL3.g:1553:3: ( ( N POINT N )=> N POINT N | POINT N | N ) ( 'E' ( PLUS | MINUS )? N )?
            pass 
            # /home/gthomas/projects/plsql/PLSQL3.g:1553:3: ( ( N POINT N )=> N POINT N | POINT N | N )
            alt6 = 3
            alt6 = self.dfa6.predict(self.input)
            if alt6 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1553:5: ( N POINT N )=> N POINT N
                pass 
                self.mN()


                self.mPOINT()


                self.mN()



            elif alt6 == 2:
                # /home/gthomas/projects/plsql/PLSQL3.g:1554:5: POINT N
                pass 
                self.mPOINT()


                self.mN()



            elif alt6 == 3:
                # /home/gthomas/projects/plsql/PLSQL3.g:1555:5: N
                pass 
                self.mN()





            # /home/gthomas/projects/plsql/PLSQL3.g:1557:3: ( 'E' ( PLUS | MINUS )? N )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 69) :
                alt8 = 1
            if alt8 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1557:5: 'E' ( PLUS | MINUS )? N
                pass 
                self.match(69)

                # /home/gthomas/projects/plsql/PLSQL3.g:1557:9: ( PLUS | MINUS )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 43 or LA7_0 == 45) :
                    alt7 = 1
                if alt7 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:
                    pass 
                    if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                self.mN()







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUMBER"



    # $ANTLR start "N"
    def mN(self, ):
        try:
            # /home/gthomas/projects/plsql/PLSQL3.g:1562:2: ( '0' .. '9' ( '0' .. '9' )* )
            # /home/gthomas/projects/plsql/PLSQL3.g:1562:4: '0' .. '9' ( '0' .. '9' )*
            pass 
            self.matchRange(48, 57)

            # /home/gthomas/projects/plsql/PLSQL3.g:1562:15: ( '0' .. '9' )*
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((48 <= LA9_0 <= 57)) :
                    alt9 = 1


                if alt9 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop9





        finally:
            pass

    # $ANTLR end "N"



    # $ANTLR start "QUOTE"
    def mQUOTE(self, ):
        try:
            _type = QUOTE
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1564:2: ( '\\'' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1564:4: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUOTE"



    # $ANTLR start "DOUBLEQUOTED_STRING"
    def mDOUBLEQUOTED_STRING(self, ):
        try:
            # /home/gthomas/projects/plsql/PLSQL3.g:1569:2: ( '\"' (~ ( '\"' ) )* '\"' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1569:4: '\"' (~ ( '\"' ) )* '\"'
            pass 
            self.match(34)

            # /home/gthomas/projects/plsql/PLSQL3.g:1569:8: (~ ( '\"' ) )*
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((0 <= LA10_0 <= 33) or (35 <= LA10_0 <= 65535)) :
                    alt10 = 1


                if alt10 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop10


            self.match(34)




        finally:
            pass

    # $ANTLR end "DOUBLEQUOTED_STRING"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1570:4: ( ( ' ' | '\\r' | '\\t' | '\\n' ) )
            # /home/gthomas/projects/plsql/PLSQL3.g:1570:6: ( ' ' | '\\r' | '\\t' | '\\n' )
            pass 
            if (9 <= self.input.LA(1) <= 10) or self.input.LA(1) == 13 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                if self._state.backtracking > 0:
                    raise BacktrackingFailed


                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            if self._state.backtracking == 0:
                pass
                _channel=HIDDEN;





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "SL_COMMENT"
    def mSL_COMMENT(self, ):
        try:
            _type = SL_COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1573:2: ( '--' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1573:4: '--' (~ ( '\\n' | '\\r' ) )* ( '\\r' )? '\\n'
            pass 
            self.match("--")


            # /home/gthomas/projects/plsql/PLSQL3.g:1573:9: (~ ( '\\n' | '\\r' ) )*
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((0 <= LA11_0 <= 9) or (11 <= LA11_0 <= 12) or (14 <= LA11_0 <= 65535)) :
                    alt11 = 1


                if alt11 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed


                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop11


            # /home/gthomas/projects/plsql/PLSQL3.g:1573:23: ( '\\r' )?
            alt12 = 2
            LA12_0 = self.input.LA(1)

            if (LA12_0 == 13) :
                alt12 = 1
            if alt12 == 1:
                # /home/gthomas/projects/plsql/PLSQL3.g:1573:23: '\\r'
                pass 
                self.match(13)




            self.match(10)

            if self._state.backtracking == 0:
                pass
                _channel=HIDDEN;





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SL_COMMENT"



    # $ANTLR start "ML_COMMENT"
    def mML_COMMENT(self, ):
        try:
            _type = ML_COMMENT
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1576:2: ( '/*' ( options {greedy=false; } : . )* '*/' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1576:4: '/*' ( options {greedy=false; } : . )* '*/'
            pass 
            self.match("/*")


            # /home/gthomas/projects/plsql/PLSQL3.g:1576:9: ( options {greedy=false; } : . )*
            while True: #loop13
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 42) :
                    LA13_1 = self.input.LA(2)

                    if (LA13_1 == 47) :
                        alt13 = 2
                    elif ((0 <= LA13_1 <= 46) or (48 <= LA13_1 <= 65535)) :
                        alt13 = 1


                elif ((0 <= LA13_0 <= 41) or (43 <= LA13_0 <= 65535)) :
                    alt13 = 1


                if alt13 == 1:
                    # /home/gthomas/projects/plsql/PLSQL3.g:1576:37: .
                    pass 
                    self.matchAny()


                else:
                    break #loop13


            self.match("*/")


            if self._state.backtracking == 0:
                pass
                _channel=HIDDEN;





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ML_COMMENT"



    # $ANTLR start "TYPE_ATTR"
    def mTYPE_ATTR(self, ):
        try:
            _type = TYPE_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1579:2: ( '%TYPE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1579:4: '%TYPE'
            pass 
            self.match("%TYPE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TYPE_ATTR"



    # $ANTLR start "ROWTYPE_ATTR"
    def mROWTYPE_ATTR(self, ):
        try:
            _type = ROWTYPE_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1582:2: ( '%ROWTYPE' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1582:4: '%ROWTYPE'
            pass 
            self.match("%ROWTYPE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROWTYPE_ATTR"



    # $ANTLR start "NOTFOUND_ATTR"
    def mNOTFOUND_ATTR(self, ):
        try:
            _type = NOTFOUND_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1585:2: ( '%NOTFOUND' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1585:4: '%NOTFOUND'
            pass 
            self.match("%NOTFOUND")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NOTFOUND_ATTR"



    # $ANTLR start "FOUND_ATTR"
    def mFOUND_ATTR(self, ):
        try:
            _type = FOUND_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1588:2: ( '%FOUND' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1588:4: '%FOUND'
            pass 
            self.match("%FOUND")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FOUND_ATTR"



    # $ANTLR start "ISOPEN_ATTR"
    def mISOPEN_ATTR(self, ):
        try:
            _type = ISOPEN_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1591:2: ( '%ISOPEN' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1591:4: '%ISOPEN'
            pass 
            self.match("%ISOPEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ISOPEN_ATTR"



    # $ANTLR start "ROWCOUNT_ATTR"
    def mROWCOUNT_ATTR(self, ):
        try:
            _type = ROWCOUNT_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1594:2: ( '%ROWCOUNT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1594:4: '%ROWCOUNT'
            pass 
            self.match("%ROWCOUNT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ROWCOUNT_ATTR"



    # $ANTLR start "BULK_ROWCOUNT_ATTR"
    def mBULK_ROWCOUNT_ATTR(self, ):
        try:
            _type = BULK_ROWCOUNT_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1597:2: ( '%BULK_ROWCOUNT' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1597:4: '%BULK_ROWCOUNT'
            pass 
            self.match("%BULK_ROWCOUNT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "BULK_ROWCOUNT_ATTR"



    # $ANTLR start "CHARSET_ATTR"
    def mCHARSET_ATTR(self, ):
        try:
            _type = CHARSET_ATTR
            _channel = DEFAULT_CHANNEL

            # /home/gthomas/projects/plsql/PLSQL3.g:1600:2: ( '%CHARSET' )
            # /home/gthomas/projects/plsql/PLSQL3.g:1600:4: '%CHARSET'
            pass 
            self.match("%CHARSET")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "CHARSET_ATTR"



    def mTokens(self):
        # /home/gthomas/projects/plsql/PLSQL3.g:1:8: ( T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | T__86 | T__87 | T__88 | T__89 | T__90 | T__91 | T__92 | T__93 | T__94 | T__95 | T__96 | T__97 | T__98 | T__99 | T__100 | T__101 | T__102 | T__103 | T__104 | T__105 | T__106 | T__107 | T__108 | T__109 | T__110 | T__111 | T__112 | T__113 | T__114 | T__115 | T__116 | T__117 | T__118 | T__119 | T__120 | T__121 | T__122 | T__123 | T__124 | T__125 | T__126 | T__127 | T__128 | T__129 | T__130 | T__131 | T__132 | T__133 | T__134 | T__135 | T__136 | T__137 | T__138 | T__139 | T__140 | T__141 | T__142 | T__143 | T__144 | T__145 | T__146 | T__147 | T__148 | T__149 | T__150 | T__151 | T__152 | T__153 | T__154 | T__155 | T__156 | T__157 | T__158 | T__159 | T__160 | T__161 | T__162 | T__163 | T__164 | T__165 | T__166 | T__167 | QUOTED_STRING | ID | SEMI | COLON | DOUBLEDOT | DOT | COMMA | EXPONENT | ASTERISK | AT_SIGN | RPAREN | LPAREN | RBRACK | LBRACK | PLUS | MINUS | DIVIDE | EQ | PERCENTAGE | LLABEL | RLABEL | ASSIGN | ARROW | VERTBAR | DOUBLEVERTBAR | NOT_EQ | LTH | LEQ | GTH | GEQ | NUMBER | QUOTE | WS | SL_COMMENT | ML_COMMENT | TYPE_ATTR | ROWTYPE_ATTR | NOTFOUND_ATTR | FOUND_ATTR | ISOPEN_ATTR | ROWCOUNT_ATTR | BULK_ROWCOUNT_ATTR | CHARSET_ATTR )
        alt14 = 161
        alt14 = self.dfa14.predict(self.input)
        if alt14 == 1:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:10: T__50
            pass 
            self.mT__50()



        elif alt14 == 2:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:16: T__51
            pass 
            self.mT__51()



        elif alt14 == 3:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:22: T__52
            pass 
            self.mT__52()



        elif alt14 == 4:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:28: T__53
            pass 
            self.mT__53()



        elif alt14 == 5:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:34: T__54
            pass 
            self.mT__54()



        elif alt14 == 6:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:40: T__55
            pass 
            self.mT__55()



        elif alt14 == 7:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:46: T__56
            pass 
            self.mT__56()



        elif alt14 == 8:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:52: T__57
            pass 
            self.mT__57()



        elif alt14 == 9:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:58: T__58
            pass 
            self.mT__58()



        elif alt14 == 10:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:64: T__59
            pass 
            self.mT__59()



        elif alt14 == 11:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:70: T__60
            pass 
            self.mT__60()



        elif alt14 == 12:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:76: T__61
            pass 
            self.mT__61()



        elif alt14 == 13:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:82: T__62
            pass 
            self.mT__62()



        elif alt14 == 14:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:88: T__63
            pass 
            self.mT__63()



        elif alt14 == 15:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:94: T__64
            pass 
            self.mT__64()



        elif alt14 == 16:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:100: T__65
            pass 
            self.mT__65()



        elif alt14 == 17:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:106: T__66
            pass 
            self.mT__66()



        elif alt14 == 18:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:112: T__67
            pass 
            self.mT__67()



        elif alt14 == 19:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:118: T__68
            pass 
            self.mT__68()



        elif alt14 == 20:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:124: T__69
            pass 
            self.mT__69()



        elif alt14 == 21:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:130: T__70
            pass 
            self.mT__70()



        elif alt14 == 22:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:136: T__71
            pass 
            self.mT__71()



        elif alt14 == 23:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:142: T__72
            pass 
            self.mT__72()



        elif alt14 == 24:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:148: T__73
            pass 
            self.mT__73()



        elif alt14 == 25:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:154: T__74
            pass 
            self.mT__74()



        elif alt14 == 26:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:160: T__75
            pass 
            self.mT__75()



        elif alt14 == 27:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:166: T__76
            pass 
            self.mT__76()



        elif alt14 == 28:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:172: T__77
            pass 
            self.mT__77()



        elif alt14 == 29:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:178: T__78
            pass 
            self.mT__78()



        elif alt14 == 30:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:184: T__79
            pass 
            self.mT__79()



        elif alt14 == 31:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:190: T__80
            pass 
            self.mT__80()



        elif alt14 == 32:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:196: T__81
            pass 
            self.mT__81()



        elif alt14 == 33:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:202: T__82
            pass 
            self.mT__82()



        elif alt14 == 34:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:208: T__83
            pass 
            self.mT__83()



        elif alt14 == 35:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:214: T__84
            pass 
            self.mT__84()



        elif alt14 == 36:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:220: T__85
            pass 
            self.mT__85()



        elif alt14 == 37:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:226: T__86
            pass 
            self.mT__86()



        elif alt14 == 38:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:232: T__87
            pass 
            self.mT__87()



        elif alt14 == 39:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:238: T__88
            pass 
            self.mT__88()



        elif alt14 == 40:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:244: T__89
            pass 
            self.mT__89()



        elif alt14 == 41:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:250: T__90
            pass 
            self.mT__90()



        elif alt14 == 42:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:256: T__91
            pass 
            self.mT__91()



        elif alt14 == 43:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:262: T__92
            pass 
            self.mT__92()



        elif alt14 == 44:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:268: T__93
            pass 
            self.mT__93()



        elif alt14 == 45:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:274: T__94
            pass 
            self.mT__94()



        elif alt14 == 46:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:280: T__95
            pass 
            self.mT__95()



        elif alt14 == 47:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:286: T__96
            pass 
            self.mT__96()



        elif alt14 == 48:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:292: T__97
            pass 
            self.mT__97()



        elif alt14 == 49:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:298: T__98
            pass 
            self.mT__98()



        elif alt14 == 50:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:304: T__99
            pass 
            self.mT__99()



        elif alt14 == 51:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:310: T__100
            pass 
            self.mT__100()



        elif alt14 == 52:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:317: T__101
            pass 
            self.mT__101()



        elif alt14 == 53:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:324: T__102
            pass 
            self.mT__102()



        elif alt14 == 54:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:331: T__103
            pass 
            self.mT__103()



        elif alt14 == 55:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:338: T__104
            pass 
            self.mT__104()



        elif alt14 == 56:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:345: T__105
            pass 
            self.mT__105()



        elif alt14 == 57:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:352: T__106
            pass 
            self.mT__106()



        elif alt14 == 58:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:359: T__107
            pass 
            self.mT__107()



        elif alt14 == 59:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:366: T__108
            pass 
            self.mT__108()



        elif alt14 == 60:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:373: T__109
            pass 
            self.mT__109()



        elif alt14 == 61:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:380: T__110
            pass 
            self.mT__110()



        elif alt14 == 62:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:387: T__111
            pass 
            self.mT__111()



        elif alt14 == 63:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:394: T__112
            pass 
            self.mT__112()



        elif alt14 == 64:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:401: T__113
            pass 
            self.mT__113()



        elif alt14 == 65:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:408: T__114
            pass 
            self.mT__114()



        elif alt14 == 66:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:415: T__115
            pass 
            self.mT__115()



        elif alt14 == 67:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:422: T__116
            pass 
            self.mT__116()



        elif alt14 == 68:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:429: T__117
            pass 
            self.mT__117()



        elif alt14 == 69:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:436: T__118
            pass 
            self.mT__118()



        elif alt14 == 70:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:443: T__119
            pass 
            self.mT__119()



        elif alt14 == 71:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:450: T__120
            pass 
            self.mT__120()



        elif alt14 == 72:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:457: T__121
            pass 
            self.mT__121()



        elif alt14 == 73:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:464: T__122
            pass 
            self.mT__122()



        elif alt14 == 74:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:471: T__123
            pass 
            self.mT__123()



        elif alt14 == 75:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:478: T__124
            pass 
            self.mT__124()



        elif alt14 == 76:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:485: T__125
            pass 
            self.mT__125()



        elif alt14 == 77:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:492: T__126
            pass 
            self.mT__126()



        elif alt14 == 78:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:499: T__127
            pass 
            self.mT__127()



        elif alt14 == 79:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:506: T__128
            pass 
            self.mT__128()



        elif alt14 == 80:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:513: T__129
            pass 
            self.mT__129()



        elif alt14 == 81:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:520: T__130
            pass 
            self.mT__130()



        elif alt14 == 82:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:527: T__131
            pass 
            self.mT__131()



        elif alt14 == 83:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:534: T__132
            pass 
            self.mT__132()



        elif alt14 == 84:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:541: T__133
            pass 
            self.mT__133()



        elif alt14 == 85:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:548: T__134
            pass 
            self.mT__134()



        elif alt14 == 86:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:555: T__135
            pass 
            self.mT__135()



        elif alt14 == 87:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:562: T__136
            pass 
            self.mT__136()



        elif alt14 == 88:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:569: T__137
            pass 
            self.mT__137()



        elif alt14 == 89:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:576: T__138
            pass 
            self.mT__138()



        elif alt14 == 90:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:583: T__139
            pass 
            self.mT__139()



        elif alt14 == 91:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:590: T__140
            pass 
            self.mT__140()



        elif alt14 == 92:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:597: T__141
            pass 
            self.mT__141()



        elif alt14 == 93:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:604: T__142
            pass 
            self.mT__142()



        elif alt14 == 94:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:611: T__143
            pass 
            self.mT__143()



        elif alt14 == 95:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:618: T__144
            pass 
            self.mT__144()



        elif alt14 == 96:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:625: T__145
            pass 
            self.mT__145()



        elif alt14 == 97:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:632: T__146
            pass 
            self.mT__146()



        elif alt14 == 98:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:639: T__147
            pass 
            self.mT__147()



        elif alt14 == 99:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:646: T__148
            pass 
            self.mT__148()



        elif alt14 == 100:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:653: T__149
            pass 
            self.mT__149()



        elif alt14 == 101:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:660: T__150
            pass 
            self.mT__150()



        elif alt14 == 102:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:667: T__151
            pass 
            self.mT__151()



        elif alt14 == 103:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:674: T__152
            pass 
            self.mT__152()



        elif alt14 == 104:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:681: T__153
            pass 
            self.mT__153()



        elif alt14 == 105:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:688: T__154
            pass 
            self.mT__154()



        elif alt14 == 106:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:695: T__155
            pass 
            self.mT__155()



        elif alt14 == 107:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:702: T__156
            pass 
            self.mT__156()



        elif alt14 == 108:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:709: T__157
            pass 
            self.mT__157()



        elif alt14 == 109:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:716: T__158
            pass 
            self.mT__158()



        elif alt14 == 110:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:723: T__159
            pass 
            self.mT__159()



        elif alt14 == 111:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:730: T__160
            pass 
            self.mT__160()



        elif alt14 == 112:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:737: T__161
            pass 
            self.mT__161()



        elif alt14 == 113:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:744: T__162
            pass 
            self.mT__162()



        elif alt14 == 114:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:751: T__163
            pass 
            self.mT__163()



        elif alt14 == 115:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:758: T__164
            pass 
            self.mT__164()



        elif alt14 == 116:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:765: T__165
            pass 
            self.mT__165()



        elif alt14 == 117:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:772: T__166
            pass 
            self.mT__166()



        elif alt14 == 118:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:779: T__167
            pass 
            self.mT__167()



        elif alt14 == 119:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:786: QUOTED_STRING
            pass 
            self.mQUOTED_STRING()



        elif alt14 == 120:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:800: ID
            pass 
            self.mID()



        elif alt14 == 121:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:803: SEMI
            pass 
            self.mSEMI()



        elif alt14 == 122:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:808: COLON
            pass 
            self.mCOLON()



        elif alt14 == 123:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:814: DOUBLEDOT
            pass 
            self.mDOUBLEDOT()



        elif alt14 == 124:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:824: DOT
            pass 
            self.mDOT()



        elif alt14 == 125:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:828: COMMA
            pass 
            self.mCOMMA()



        elif alt14 == 126:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:834: EXPONENT
            pass 
            self.mEXPONENT()



        elif alt14 == 127:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:843: ASTERISK
            pass 
            self.mASTERISK()



        elif alt14 == 128:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:852: AT_SIGN
            pass 
            self.mAT_SIGN()



        elif alt14 == 129:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:860: RPAREN
            pass 
            self.mRPAREN()



        elif alt14 == 130:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:867: LPAREN
            pass 
            self.mLPAREN()



        elif alt14 == 131:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:874: RBRACK
            pass 
            self.mRBRACK()



        elif alt14 == 132:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:881: LBRACK
            pass 
            self.mLBRACK()



        elif alt14 == 133:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:888: PLUS
            pass 
            self.mPLUS()



        elif alt14 == 134:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:893: MINUS
            pass 
            self.mMINUS()



        elif alt14 == 135:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:899: DIVIDE
            pass 
            self.mDIVIDE()



        elif alt14 == 136:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:906: EQ
            pass 
            self.mEQ()



        elif alt14 == 137:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:909: PERCENTAGE
            pass 
            self.mPERCENTAGE()



        elif alt14 == 138:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:920: LLABEL
            pass 
            self.mLLABEL()



        elif alt14 == 139:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:927: RLABEL
            pass 
            self.mRLABEL()



        elif alt14 == 140:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:934: ASSIGN
            pass 
            self.mASSIGN()



        elif alt14 == 141:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:941: ARROW
            pass 
            self.mARROW()



        elif alt14 == 142:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:947: VERTBAR
            pass 
            self.mVERTBAR()



        elif alt14 == 143:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:955: DOUBLEVERTBAR
            pass 
            self.mDOUBLEVERTBAR()



        elif alt14 == 144:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:969: NOT_EQ
            pass 
            self.mNOT_EQ()



        elif alt14 == 145:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:976: LTH
            pass 
            self.mLTH()



        elif alt14 == 146:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:980: LEQ
            pass 
            self.mLEQ()



        elif alt14 == 147:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:984: GTH
            pass 
            self.mGTH()



        elif alt14 == 148:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:988: GEQ
            pass 
            self.mGEQ()



        elif alt14 == 149:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:992: NUMBER
            pass 
            self.mNUMBER()



        elif alt14 == 150:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:999: QUOTE
            pass 
            self.mQUOTE()



        elif alt14 == 151:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1005: WS
            pass 
            self.mWS()



        elif alt14 == 152:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1008: SL_COMMENT
            pass 
            self.mSL_COMMENT()



        elif alt14 == 153:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1019: ML_COMMENT
            pass 
            self.mML_COMMENT()



        elif alt14 == 154:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1030: TYPE_ATTR
            pass 
            self.mTYPE_ATTR()



        elif alt14 == 155:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1040: ROWTYPE_ATTR
            pass 
            self.mROWTYPE_ATTR()



        elif alt14 == 156:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1053: NOTFOUND_ATTR
            pass 
            self.mNOTFOUND_ATTR()



        elif alt14 == 157:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1067: FOUND_ATTR
            pass 
            self.mFOUND_ATTR()



        elif alt14 == 158:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1078: ISOPEN_ATTR
            pass 
            self.mISOPEN_ATTR()



        elif alt14 == 159:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1090: ROWCOUNT_ATTR
            pass 
            self.mROWCOUNT_ATTR()



        elif alt14 == 160:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1104: BULK_ROWCOUNT_ATTR
            pass 
            self.mBULK_ROWCOUNT_ATTR()



        elif alt14 == 161:
            # /home/gthomas/projects/plsql/PLSQL3.g:1:1123: CHARSET_ATTR
            pass 
            self.mCHARSET_ATTR()







    # $ANTLR start "synpred1_PLSQL3"
    def synpred1_PLSQL3_fragment(self, ):
        # /home/gthomas/projects/plsql/PLSQL3.g:1553:5: ( N POINT N )
        # /home/gthomas/projects/plsql/PLSQL3.g:1553:7: N POINT N
        pass 
        self.mN()


        self.mPOINT()


        self.mN()




    # $ANTLR end "synpred1_PLSQL3"



    def synpred1_PLSQL3(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_PLSQL3_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



    # lookup tables for DFA #6

    DFA6_eot = DFA.unpack(
        u"\1\uffff\1\4\1\uffff\1\4\2\uffff"
        )

    DFA6_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA6_min = DFA.unpack(
        u"\2\56\1\uffff\1\56\2\uffff"
        )

    DFA6_max = DFA.unpack(
        u"\2\71\1\uffff\1\71\2\uffff"
        )

    DFA6_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\3\1\1"
        )

    DFA6_special = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\0\2\uffff"
        )


    DFA6_transition = [
        DFA.unpack(u"\1\2\1\uffff\12\1"),
        DFA.unpack(u"\1\5\1\uffff\12\3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\5\1\uffff\12\3"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #6

    class DFA6(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA6_3 = input.LA(1)

                 
                index6_3 = input.index()
                input.rewind()

                s = -1
                if (LA6_3 == 46) and (self.synpred1_PLSQL3()):
                    s = 5

                elif ((48 <= LA6_3 <= 57)):
                    s = 3

                else:
                    s = 4

                 
                input.seek(index6_3)

                if s >= 0:
                    return s
            el
            if s == 1: 
                LA6_1 = input.LA(1)

                 
                index6_1 = input.index()
                input.rewind()

                s = -1
                if ((48 <= LA6_1 <= 57)):
                    s = 3

                elif (LA6_1 == 46) and (self.synpred1_PLSQL3()):
                    s = 5

                else:
                    s = 4

                 
                input.seek(index6_1)

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 6, _s, input)
            self_.error(nvae)
            raise nvae

    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        u"\1\uffff\24\27\1\uffff\1\164\2\uffff\1\166\1\167\1\uffff\1\172"
        u"\6\uffff\1\174\1\176\1\u0080\1\u0088\1\u008b\1\u008e\1\u0090\3"
        u"\uffff\2\27\1\u0095\1\u0096\5\27\1\u009d\25\27\1\u00b8\1\u00bc"
        u"\1\u00bd\12\27\1\u00cd\1\u00ce\1\u00d0\20\27\1\u00e8\7\27\35\uffff"
        u"\1\u00f3\1\u00f4\1\u00f5\1\u00f6\2\uffff\6\27\1\uffff\7\27\1\u0107"
        u"\6\27\1\u010f\5\27\1\u0116\5\27\1\uffff\2\27\1\u0120\2\uffff\12"
        u"\27\1\u012c\4\27\2\uffff\1\27\1\uffff\1\u0133\7\27\1\u013b\4\27"
        u"\1\u0142\2\27\1\u0145\2\27\1\u0148\3\27\1\uffff\11\27\5\uffff\4"
        u"\27\1\u015c\1\27\1\u015e\1\u0160\1\u0161\4\27\1\u0167\2\27\1\uffff"
        u"\2\27\1\u016c\2\27\1\u016f\1\27\1\uffff\6\27\1\uffff\1\u0177\1"
        u"\27\1\u0179\5\27\1\u0180\1\uffff\1\u0181\1\u0182\1\u0183\1\u0184"
        u"\2\27\1\u0187\4\27\1\uffff\1\27\1\u018d\4\27\1\uffff\7\27\1\uffff"
        u"\1\u0199\4\27\1\u019e\1\uffff\2\27\1\uffff\2\27\1\uffff\2\27\1"
        u"\u01a5\1\u01a6\6\27\1\u01ad\2\27\1\u01b0\1\uffff\1\u01b3\1\27\1"
        u"\u01b5\1\27\1\uffff\1\27\1\uffff\1\27\2\uffff\5\27\1\uffff\4\27"
        u"\1\uffff\2\27\1\uffff\1\u01c4\3\27\1\u01c8\1\u01c9\1\u01ca\1\uffff"
        u"\1\27\1\uffff\1\u01cc\1\27\1\u01ce\3\27\5\uffff\1\u01d2\1\27\1"
        u"\uffff\2\27\1\u01d6\1\u01d7\1\27\1\uffff\3\27\1\u01dc\4\27\1\u01e1"
        u"\1\27\1\u01e3\1\uffff\3\27\1\u01e7\1\uffff\2\27\1\u01ea\1\27\1"
        u"\u01ec\1\u01ed\2\uffff\1\u01ee\5\27\1\uffff\1\u01f4\1\u01f5\4\uffff"
        u"\1\27\1\uffff\4\27\1\u01fb\2\27\1\u01fe\3\27\1\u0202\1\27\1\u0204"
        u"\1\uffff\2\27\1\u0207\3\uffff\1\27\1\uffff\1\u0209\1\uffff\1\u020a"
        u"\2\27\1\uffff\3\27\2\uffff\1\u0210\1\u0211\2\27\1\uffff\3\27\1"
        u"\u0217\1\uffff\1\27\1\uffff\1\u0219\1\u021b\1\27\1\uffff\1\27\1"
        u"\u021e\1\uffff\1\27\3\uffff\1\u0220\1\u0221\1\u0222\1\u0223\1\27"
        u"\2\uffff\1\u0225\1\27\1\u0229\1\27\1\u022b\1\uffff\1\u022c\1\27"
        u"\1\uffff\1\u022e\1\u022f\1\u0230\1\uffff\1\27\1\uffff\2\27\1\uffff"
        u"\1\27\2\uffff\1\u0235\3\27\1\u0239\2\uffff\1\u023a\1\27\1\u023c"
        u"\2\27\1\uffff\1\27\1\uffff\1\27\1\uffff\2\27\1\uffff\1\27\4\uffff"
        u"\1\u0245\1\uffff\3\27\1\uffff\1\27\2\uffff\1\u024a\3\uffff\1\u024b"
        u"\2\27\1\u024e\1\uffff\1\27\1\u0250\1\u0251\2\uffff\1\u0253\1\uffff"
        u"\1\27\1\u0255\2\27\1\u0258\1\27\1\u025a\1\u025b\1\uffff\3\27\1"
        u"\u025f\2\uffff\1\u0260\1\u0261\1\uffff\1\u0262\2\uffff\1\u0263"
        u"\1\uffff\1\27\1\uffff\1\u0265\1\u0266\1\uffff\1\u0267\2\uffff\3"
        u"\27\5\uffff\1\27\3\uffff\3\27\1\u026f\1\27\1\u0271\1\27\1\uffff"
        u"\1\u0273\1\uffff\1\27\1\uffff\1\u0275\1\uffff"
        )

    DFA14_eof = DFA.unpack(
        u"\u0276\uffff"
        )

    DFA14_min = DFA.unpack(
        u"\1\11\1\114\1\105\2\101\1\114\1\101\1\117\1\101\1\106\2\111\1\101"
        u"\1\106\4\101\1\116\1\101\1\110\1\uffff\1\0\2\uffff\1\75\1\56\1"
        u"\uffff\1\52\6\uffff\1\55\1\52\1\76\1\102\1\74\1\75\1\174\3\uffff"
        u"\1\114\1\104\2\43\1\107\1\111\1\116\2\117\1\43\1\123\1\101\1\117"
        u"\1\115\1\105\1\124\1\103\1\123\1\125\1\123\1\104\1\103\1\114\1"
        u"\124\1\117\1\122\1\117\1\116\1\124\1\117\1\126\3\43\1\113\1\103"
        u"\1\116\1\123\1\104\1\124\1\110\1\124\1\114\1\101\3\43\1\124\1\103"
        u"\2\123\1\101\1\111\1\101\1\114\1\126\1\114\2\101\1\114\1\101\1"
        u"\102\1\105\1\43\1\125\1\111\1\104\1\117\1\114\1\105\1\124\16\uffff"
        u"\1\117\16\uffff\4\43\2\uffff\1\111\1\127\1\114\1\101\1\102\1\114"
        u"\1\uffff\1\105\1\122\1\102\1\115\1\116\1\101\1\105\1\43\1\101\1"
        u"\105\1\103\1\124\1\102\1\105\1\43\1\105\2\123\1\103\1\101\1\43"
        u"\1\115\1\103\1\117\1\125\1\111\1\uffff\2\105\1\43\2\uffff\1\105"
        u"\1\113\1\107\1\120\1\125\1\114\1\105\1\111\1\101\1\117\1\43\1\101"
        u"\1\114\1\102\1\122\2\uffff\1\105\1\uffff\1\43\1\113\1\137\1\111"
        u"\1\107\1\117\1\103\1\123\1\43\1\114\1\117\1\125\1\114\1\43\2\105"
        u"\1\43\1\122\1\114\1\43\1\122\1\114\1\116\1\uffff\1\105\1\117\1"
        u"\101\1\127\1\125\1\103\1\116\1\114\1\110\1\127\4\uffff\1\116\2"
        u"\105\1\122\1\43\1\105\3\43\2\105\2\124\1\43\1\115\1\101\1\uffff"
        u"\1\125\1\124\1\43\1\111\1\114\1\43\1\106\1\uffff\1\120\1\125\1"
        u"\124\1\105\1\110\1\124\1\uffff\1\43\1\124\1\43\1\120\1\116\1\130"
        u"\1\122\1\107\1\43\1\uffff\4\43\1\123\1\101\1\43\1\117\2\122\1\102"
        u"\1\uffff\1\111\1\43\1\105\1\122\1\103\1\122\1\uffff\1\101\1\111"
        u"\1\124\1\115\1\122\2\105\1\uffff\1\43\2\122\1\102\1\104\1\43\1"
        u"\uffff\1\120\1\103\1\uffff\1\105\1\114\1\uffff\1\124\1\105\2\43"
        u"\1\116\1\125\1\124\1\111\1\105\1\110\1\43\2\105\1\43\1\103\1\43"
        u"\1\105\1\43\1\131\1\uffff\1\101\1\uffff\1\103\2\uffff\1\116\1\124"
        u"\1\103\1\101\1\105\1\uffff\1\101\1\122\1\114\1\105\1\uffff\1\116"
        u"\1\105\1\uffff\1\43\1\124\2\123\3\43\1\uffff\1\111\1\uffff\1\43"
        u"\1\107\1\43\1\124\1\105\1\123\5\uffff\1\43\1\102\1\uffff\1\116"
        u"\1\101\2\43\1\124\1\uffff\1\122\1\111\1\110\1\43\1\107\1\116\1"
        u"\111\1\101\1\43\1\104\1\43\1\uffff\1\104\1\116\1\101\1\43\1\uffff"
        u"\1\117\1\124\1\43\1\111\2\43\2\uffff\1\43\2\105\1\104\1\123\1\101"
        u"\1\uffff\2\43\4\uffff\1\116\1\uffff\1\137\1\116\2\124\1\43\1\124"
        u"\1\116\1\43\1\114\1\105\1\124\1\43\1\103\1\43\1\uffff\2\111\1\43"
        u"\3\uffff\1\117\1\uffff\1\43\1\uffff\1\43\1\122\1\105\1\uffff\1"
        u"\105\1\101\1\114\2\uffff\2\43\1\103\1\101\1\uffff\1\105\1\124\1"
        u"\126\1\43\1\uffff\1\125\1\uffff\2\43\1\103\1\uffff\1\111\1\43\1"
        u"\uffff\1\116\3\uffff\4\43\1\122\2\uffff\1\43\1\104\1\43\1\105\1"
        u"\43\1\uffff\1\43\1\124\1\uffff\3\43\1\uffff\1\124\1\uffff\1\117"
        u"\1\126\1\uffff\1\116\2\uffff\1\43\1\103\2\114\1\43\2\uffff\1\43"
        u"\1\122\1\43\2\105\1\uffff\1\122\1\uffff\1\116\1\uffff\1\113\1\116"
        u"\1\uffff\1\124\4\uffff\1\43\1\uffff\1\117\1\114\1\116\1\uffff\1"
        u"\122\2\uffff\1\43\3\uffff\1\43\1\116\1\105\1\43\1\uffff\1\124\2"
        u"\43\2\uffff\1\43\1\uffff\1\107\1\43\1\105\1\107\1\43\1\124\2\43"
        u"\1\uffff\1\125\1\117\1\124\1\43\2\uffff\2\43\1\uffff\1\43\2\uffff"
        u"\1\43\1\uffff\1\105\1\uffff\2\43\1\uffff\1\43\2\uffff\1\102\1\101"
        u"\1\105\5\uffff\1\122\3\uffff\1\114\1\124\1\107\1\43\1\105\1\43"
        u"\1\105\1\uffff\1\43\1\uffff\1\122\1\uffff\1\43\1\uffff"
        )

    DFA14_max = DFA.unpack(
        u"\1\174\1\124\1\131\1\122\1\117\1\130\1\125\1\122\1\101\1\123\2"
        u"\117\1\126\1\125\1\122\1\117\1\124\2\122\1\101\1\111\1\uffff\1"
        u"\uffff\2\uffff\1\75\1\71\1\uffff\1\52\6\uffff\1\55\1\52\1\76\1"
        u"\124\2\76\1\174\3\uffff\1\114\1\131\2\137\1\124\1\111\1\116\2\117"
        u"\1\137\1\123\1\101\1\117\1\116\1\105\1\124\2\123\1\125\1\123\1"
        u"\104\1\111\1\114\1\124\1\117\1\122\1\117\1\116\1\124\1\117\1\126"
        u"\3\137\1\113\1\117\1\116\1\123\1\104\1\124\1\114\1\127\1\115\1"
        u"\101\3\137\1\124\1\103\2\123\1\117\1\127\1\124\1\127\1\126\1\124"
        u"\2\101\1\114\1\101\1\102\1\105\1\137\1\125\1\111\1\104\1\117\1"
        u"\122\1\111\1\124\16\uffff\1\117\16\uffff\4\137\2\uffff\1\111\1"
        u"\127\1\114\1\101\1\102\1\114\1\uffff\1\105\1\122\1\102\1\115\1"
        u"\123\1\101\1\105\1\137\1\101\1\105\1\103\1\124\1\102\1\111\1\137"
        u"\1\114\2\123\1\103\1\101\1\137\1\115\1\103\1\117\1\125\1\111\1"
        u"\uffff\2\105\1\137\2\uffff\1\105\1\113\1\107\1\120\1\125\1\114"
        u"\1\105\1\125\1\101\1\117\1\137\1\101\1\114\1\105\1\122\2\uffff"
        u"\1\105\1\uffff\1\137\1\113\1\137\1\111\1\107\1\117\1\103\1\123"
        u"\1\137\1\114\1\117\1\125\1\114\1\137\2\105\1\137\1\122\1\114\1"
        u"\137\1\122\1\114\1\116\1\uffff\1\105\1\121\1\101\1\127\1\125\1"
        u"\103\1\122\1\114\1\110\1\127\4\uffff\1\116\2\105\1\122\1\137\1"
        u"\105\3\137\1\111\1\105\2\124\1\137\1\115\1\101\1\uffff\1\125\1"
        u"\124\1\137\1\111\1\114\1\137\1\106\1\uffff\1\120\1\125\1\124\1"
        u"\105\1\110\1\124\1\uffff\1\137\1\124\1\137\1\120\1\116\1\130\2"
        u"\122\1\137\1\uffff\4\137\1\123\1\101\1\137\1\117\2\122\1\102\1"
        u"\uffff\1\111\1\137\1\105\1\122\1\103\1\122\1\uffff\1\101\1\111"
        u"\1\124\1\115\1\122\2\105\1\uffff\1\137\2\122\1\102\1\104\1\137"
        u"\1\uffff\1\120\1\103\1\uffff\1\105\1\114\1\uffff\1\124\1\105\2"
        u"\137\1\116\1\125\1\124\1\111\1\105\1\110\1\137\2\105\1\137\1\124"
        u"\1\137\1\105\1\137\1\131\1\uffff\1\101\1\uffff\1\103\2\uffff\1"
        u"\116\1\124\1\103\1\101\1\105\1\uffff\1\101\1\122\1\114\1\105\1"
        u"\uffff\1\116\1\105\1\uffff\1\137\1\124\2\123\3\137\1\uffff\1\111"
        u"\1\uffff\1\137\1\107\1\137\1\124\1\105\1\123\5\uffff\1\137\1\102"
        u"\1\uffff\1\116\1\101\2\137\1\124\1\uffff\1\122\1\111\1\110\1\137"
        u"\1\107\1\116\1\111\1\101\1\137\1\104\1\137\1\uffff\1\104\1\116"
        u"\1\101\1\137\1\uffff\1\117\1\124\1\137\1\111\2\137\2\uffff\1\137"
        u"\2\105\1\104\1\123\1\101\1\uffff\2\137\4\uffff\1\116\1\uffff\1"
        u"\137\1\116\2\124\1\137\1\124\1\116\1\137\1\114\1\105\1\124\1\137"
        u"\1\103\1\137\1\uffff\2\111\1\137\3\uffff\1\117\1\uffff\1\137\1"
        u"\uffff\1\137\1\122\1\105\1\uffff\1\105\1\101\1\114\2\uffff\2\137"
        u"\1\103\1\101\1\uffff\1\105\1\124\1\126\1\137\1\uffff\1\125\1\uffff"
        u"\2\137\1\103\1\uffff\1\111\1\137\1\uffff\1\116\3\uffff\4\137\1"
        u"\122\2\uffff\1\137\1\111\1\137\1\105\1\137\1\uffff\1\137\1\124"
        u"\1\uffff\3\137\1\uffff\1\124\1\uffff\1\117\1\126\1\uffff\1\116"
        u"\2\uffff\1\137\1\103\2\114\1\137\2\uffff\1\137\1\122\1\137\2\105"
        u"\1\uffff\1\122\1\uffff\1\116\1\uffff\1\113\1\116\1\uffff\1\124"
        u"\4\uffff\1\137\1\uffff\1\117\1\114\1\116\1\uffff\1\122\2\uffff"
        u"\1\137\3\uffff\1\137\1\116\1\105\1\137\1\uffff\1\124\2\137\2\uffff"
        u"\1\137\1\uffff\1\107\1\137\1\105\1\107\1\137\1\124\2\137\1\uffff"
        u"\1\125\1\117\1\124\1\137\2\uffff\2\137\1\uffff\1\137\2\uffff\1"
        u"\137\1\uffff\1\105\1\uffff\2\137\1\uffff\1\137\2\uffff\1\102\1"
        u"\101\1\105\5\uffff\1\122\3\uffff\1\114\1\124\1\107\1\137\1\105"
        u"\1\137\1\105\1\uffff\1\137\1\uffff\1\122\1\uffff\1\137\1\uffff"
        )

    DFA14_accept = DFA.unpack(
        u"\25\uffff\1\167\1\uffff\1\170\1\171\2\uffff\1\175\1\uffff\1\u0080"
        u"\1\u0081\1\u0082\1\u0083\1\u0084\1\u0085\7\uffff\1\u0090\1\u0095"
        u"\1\u0097\107\uffff\1\u0096\1\u008c\1\172\1\174\1\173\1\176\1\177"
        u"\1\u0098\1\u0086\1\u0099\1\u0087\1\u008d\1\u0088\1\u009a\1\uffff"
        u"\1\u009c\1\u009d\1\u009e\1\u00a0\1\u00a1\1\u0089\1\u008a\1\u0092"
        u"\1\u0091\1\u008b\1\u0094\1\u0093\1\u008f\1\u008e\4\uffff\1\4\1"
        u"\6\6\uffff\1\17\32\uffff\1\61\3\uffff\1\62\1\71\17\uffff\1\114"
        u"\1\115\1\uffff\1\116\27\uffff\1\152\12\uffff\1\1\1\2\1\3\1\5\20"
        u"\uffff\1\32\7\uffff\1\44\6\uffff\1\53\11\uffff\1\65\13\uffff\1"
        u"\105\6\uffff\1\120\7\uffff\1\130\6\uffff\1\136\2\uffff\1\143\2"
        u"\uffff\1\146\23\uffff\1\15\1\uffff\1\20\1\uffff\1\21\1\23\5\uffff"
        u"\1\31\4\uffff\1\37\2\uffff\1\42\7\uffff\1\54\1\uffff\1\56\6\uffff"
        u"\1\70\1\72\1\73\1\74\1\75\2\uffff\1\100\5\uffff\1\107\13\uffff"
        u"\1\131\4\uffff\1\140\6\uffff\1\151\1\153\6\uffff\1\163\2\uffff"
        u"\1\166\1\u009b\1\u009f\1\7\1\uffff\1\11\16\uffff\1\43\3\uffff\1"
        u"\50\1\51\1\52\1\uffff\1\57\1\uffff\1\63\3\uffff\1\76\3\uffff\1"
        u"\103\1\104\4\uffff\1\117\4\uffff\1\125\1\uffff\1\127\3\uffff\1"
        u"\137\2\uffff\1\144\1\uffff\1\147\1\150\1\154\5\uffff\1\164\1\165"
        u"\5\uffff\1\25\2\uffff\1\30\3\uffff\1\36\1\uffff\1\41\2\uffff\1"
        u"\47\1\uffff\1\60\1\64\5\uffff\1\106\1\110\5\uffff\1\124\1\uffff"
        u"\1\132\1\uffff\1\133\2\uffff\1\142\1\uffff\1\155\1\156\1\157\1"
        u"\160\1\uffff\1\10\3\uffff\1\16\1\uffff\1\24\1\26\1\uffff\1\33\1"
        u"\34\1\35\4\uffff\1\66\3\uffff\1\102\1\111\1\uffff\1\121\10\uffff"
        u"\1\161\4\uffff\1\27\1\40\2\uffff\1\55\1\uffff\1\77\1\101\1\uffff"
        u"\1\112\1\uffff\1\123\2\uffff\1\135\1\uffff\1\145\1\162\3\uffff"
        u"\1\22\1\45\1\46\1\67\1\113\1\uffff\1\126\1\134\1\141\7\uffff\1"
        u"\122\1\uffff\1\13\1\uffff\1\12\1\uffff\1\14"
        )

    DFA14_special = DFA.unpack(
        u"\26\uffff\1\0\u025f\uffff"
        )


    DFA14_transition = [
        DFA.unpack(u"\2\54\2\uffff\1\54\22\uffff\1\54\1\52\1\27\2\uffff\1"
        u"\46\1\uffff\1\26\1\37\1\36\1\34\1\42\1\33\1\43\1\32\1\44\12\53"
        u"\1\31\1\30\1\47\1\45\1\50\1\uffff\1\35\1\1\1\2\1\3\1\4\1\5\1\6"
        u"\1\7\1\10\1\11\2\27\1\12\1\13\1\14\1\15\1\16\1\27\1\17\1\20\1\21"
        u"\1\22\1\23\1\24\3\27\1\41\1\uffff\1\40\1\52\17\uffff\1\25\15\uffff"
        u"\1\51"),
        DFA.unpack(u"\1\55\1\uffff\1\56\4\uffff\1\57\1\60"),
        DFA.unpack(u"\1\61\1\62\2\uffff\1\63\2\uffff\1\64\2\uffff\1\65\11"
        u"\uffff\1\66"),
        DFA.unpack(u"\1\67\6\uffff\1\70\3\uffff\1\71\2\uffff\1\72\2\uffff"
        u"\1\73"),
        DFA.unpack(u"\1\74\3\uffff\1\75\3\uffff\1\76\5\uffff\1\77"),
        DFA.unpack(u"\1\100\1\uffff\1\101\11\uffff\1\102"),
        DFA.unpack(u"\1\103\3\uffff\1\104\6\uffff\1\105\2\uffff\1\106\2"
        u"\uffff\1\107\2\uffff\1\110"),
        DFA.unpack(u"\1\111\2\uffff\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\114\7\uffff\1\115\4\uffff\1\116"),
        DFA.unpack(u"\1\117\5\uffff\1\120"),
        DFA.unpack(u"\1\121\2\uffff\1\122\2\uffff\1\123"),
        DFA.unpack(u"\1\124\1\uffff\1\125\13\uffff\1\126\5\uffff\1\127\1"
        u"\130"),
        DFA.unpack(u"\1\131\7\uffff\1\132\3\uffff\1\133\2\uffff\1\134"),
        DFA.unpack(u"\1\135\12\uffff\1\136\2\uffff\1\137\2\uffff\1\140"),
        DFA.unpack(u"\1\141\3\uffff\1\142\11\uffff\1\143"),
        DFA.unpack(u"\1\144\3\uffff\1\145\2\uffff\1\146\4\uffff\1\147\3"
        u"\uffff\1\150\2\uffff\1\151"),
        DFA.unpack(u"\1\152\6\uffff\1\153\6\uffff\1\154\2\uffff\1\155"),
        DFA.unpack(u"\1\156\1\uffff\1\157\1\uffff\1\160"),
        DFA.unpack(u"\1\161"),
        DFA.unpack(u"\1\162\1\163"),
        DFA.unpack(u""),
        DFA.unpack(u"\0\25"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\165"),
        DFA.unpack(u"\1\170\1\uffff\12\53"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\171"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\173"),
        DFA.unpack(u"\1\175"),
        DFA.unpack(u"\1\177"),
        DFA.unpack(u"\1\u0086\1\u0087\2\uffff\1\u0084\2\uffff\1\u0085\4"
        u"\uffff\1\u0083\3\uffff\1\u0082\1\uffff\1\u0081"),
        DFA.unpack(u"\1\u0089\1\u008a\1\52"),
        DFA.unpack(u"\1\u008d\1\u008c"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092\24\uffff\1\u0093"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\2\27\1\u0094\27\27\4\uffff"
        u"\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0097\14\uffff\1\u0098"),
        DFA.unpack(u"\1\u0099"),
        DFA.unpack(u"\1\u009a"),
        DFA.unpack(u"\1\u009b"),
        DFA.unpack(u"\1\u009c"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u009e"),
        DFA.unpack(u"\1\u009f"),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1\1\u00a2"),
        DFA.unpack(u"\1\u00a3"),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5\2\uffff\1\u00a6\5\uffff\1\u00a7\6\uffff\1"
        u"\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad\5\uffff\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u"\1\u00b1"),
        DFA.unpack(u"\1\u00b2"),
        DFA.unpack(u"\1\u00b3"),
        DFA.unpack(u"\1\u00b4"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\3\27\1\u00b9\16\27\1\u00ba"
        u"\1\u00bb\6\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf\12\uffff\1\u00c0\1\u00c1"),
        DFA.unpack(u"\1\u00c2"),
        DFA.unpack(u"\1\u00c3"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u"\1\u00c5"),
        DFA.unpack(u"\1\u00c6\3\uffff\1\u00c7"),
        DFA.unpack(u"\1\u00c8\2\uffff\1\u00c9"),
        DFA.unpack(u"\1\u00ca\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\3\27\1\u00cf\26\27\4\uffff"
        u"\1\27"),
        DFA.unpack(u"\1\u00d1"),
        DFA.unpack(u"\1\u00d2"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\1\u00d5\7\uffff\1\u00d6\5\uffff\1\u00d7"),
        DFA.unpack(u"\1\u00d8\15\uffff\1\u00d9"),
        DFA.unpack(u"\1\u00da\1\uffff\1\u00db\20\uffff\1\u00dc"),
        DFA.unpack(u"\1\u00dd\12\uffff\1\u00de"),
        DFA.unpack(u"\1\u00df"),
        DFA.unpack(u"\1\u00e0\7\uffff\1\u00e1"),
        DFA.unpack(u"\1\u00e2"),
        DFA.unpack(u"\1\u00e3"),
        DFA.unpack(u"\1\u00e4"),
        DFA.unpack(u"\1\u00e5"),
        DFA.unpack(u"\1\u00e6"),
        DFA.unpack(u"\1\u00e7"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u00e9"),
        DFA.unpack(u"\1\u00ea"),
        DFA.unpack(u"\1\u00eb"),
        DFA.unpack(u"\1\u00ec"),
        DFA.unpack(u"\1\u00ed\5\uffff\1\u00ee"),
        DFA.unpack(u"\1\u00ef\3\uffff\1\u00f0"),
        DFA.unpack(u"\1\u00f1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00f7"),
        DFA.unpack(u"\1\u00f8"),
        DFA.unpack(u"\1\u00f9"),
        DFA.unpack(u"\1\u00fa"),
        DFA.unpack(u"\1\u00fb"),
        DFA.unpack(u"\1\u00fc"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00fd"),
        DFA.unpack(u"\1\u00fe"),
        DFA.unpack(u"\1\u00ff"),
        DFA.unpack(u"\1\u0100"),
        DFA.unpack(u"\1\u0101\4\uffff\1\u0102"),
        DFA.unpack(u"\1\u0103"),
        DFA.unpack(u"\1\u0104"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\10\27\1\u0105\2\27\1\u0106"
        u"\16\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0108"),
        DFA.unpack(u"\1\u0109"),
        DFA.unpack(u"\1\u010a"),
        DFA.unpack(u"\1\u010b"),
        DFA.unpack(u"\1\u010c"),
        DFA.unpack(u"\1\u010d\3\uffff\1\u010e"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0110\6\uffff\1\u0111"),
        DFA.unpack(u"\1\u0112"),
        DFA.unpack(u"\1\u0113"),
        DFA.unpack(u"\1\u0114"),
        DFA.unpack(u"\1\u0115"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0117"),
        DFA.unpack(u"\1\u0118"),
        DFA.unpack(u"\1\u0119"),
        DFA.unpack(u"\1\u011a"),
        DFA.unpack(u"\1\u011b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u011c"),
        DFA.unpack(u"\1\u011d"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\4\27\1\u011e\11\27\1\u011f"
        u"\13\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0121"),
        DFA.unpack(u"\1\u0122"),
        DFA.unpack(u"\1\u0123"),
        DFA.unpack(u"\1\u0124"),
        DFA.unpack(u"\1\u0125"),
        DFA.unpack(u"\1\u0126"),
        DFA.unpack(u"\1\u0127"),
        DFA.unpack(u"\1\u0128\13\uffff\1\u0129"),
        DFA.unpack(u"\1\u012a"),
        DFA.unpack(u"\1\u012b"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u012d"),
        DFA.unpack(u"\1\u012e"),
        DFA.unpack(u"\1\u012f\2\uffff\1\u0130"),
        DFA.unpack(u"\1\u0131"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0132"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0134"),
        DFA.unpack(u"\1\u0135"),
        DFA.unpack(u"\1\u0136"),
        DFA.unpack(u"\1\u0137"),
        DFA.unpack(u"\1\u0138"),
        DFA.unpack(u"\1\u0139"),
        DFA.unpack(u"\1\u013a"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u013c"),
        DFA.unpack(u"\1\u013d"),
        DFA.unpack(u"\1\u013e"),
        DFA.unpack(u"\1\u013f"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\10\27\1\u0140\11\27\1"
        u"\u0141\7\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0143"),
        DFA.unpack(u"\1\u0144"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0146"),
        DFA.unpack(u"\1\u0147"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0149"),
        DFA.unpack(u"\1\u014a"),
        DFA.unpack(u"\1\u014b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u014c"),
        DFA.unpack(u"\1\u014d\1\uffff\1\u014e"),
        DFA.unpack(u"\1\u014f"),
        DFA.unpack(u"\1\u0150"),
        DFA.unpack(u"\1\u0151"),
        DFA.unpack(u"\1\u0152"),
        DFA.unpack(u"\1\u0153\3\uffff\1\u0154"),
        DFA.unpack(u"\1\u0155"),
        DFA.unpack(u"\1\u0156"),
        DFA.unpack(u"\1\u0157"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0158"),
        DFA.unpack(u"\1\u0159"),
        DFA.unpack(u"\1\u015a"),
        DFA.unpack(u"\1\u015b"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u015d"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\1\u015f\31\27\4\uffff"
        u"\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0162\3\uffff\1\u0163"),
        DFA.unpack(u"\1\u0164"),
        DFA.unpack(u"\1\u0165"),
        DFA.unpack(u"\1\u0166"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0168"),
        DFA.unpack(u"\1\u0169"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u016a"),
        DFA.unpack(u"\1\u016b"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u016d"),
        DFA.unpack(u"\1\u016e"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0170"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0171"),
        DFA.unpack(u"\1\u0172"),
        DFA.unpack(u"\1\u0173"),
        DFA.unpack(u"\1\u0174"),
        DFA.unpack(u"\1\u0175"),
        DFA.unpack(u"\1\u0176"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0178"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u017a"),
        DFA.unpack(u"\1\u017b"),
        DFA.unpack(u"\1\u017c"),
        DFA.unpack(u"\1\u017d"),
        DFA.unpack(u"\1\u017e\12\uffff\1\u017f"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0185"),
        DFA.unpack(u"\1\u0186"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0188"),
        DFA.unpack(u"\1\u0189"),
        DFA.unpack(u"\1\u018a"),
        DFA.unpack(u"\1\u018b"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u018c"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u018e"),
        DFA.unpack(u"\1\u018f"),
        DFA.unpack(u"\1\u0190"),
        DFA.unpack(u"\1\u0191"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0192"),
        DFA.unpack(u"\1\u0193"),
        DFA.unpack(u"\1\u0194"),
        DFA.unpack(u"\1\u0195"),
        DFA.unpack(u"\1\u0196"),
        DFA.unpack(u"\1\u0197"),
        DFA.unpack(u"\1\u0198"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u019a"),
        DFA.unpack(u"\1\u019b"),
        DFA.unpack(u"\1\u019c"),
        DFA.unpack(u"\1\u019d"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u019f"),
        DFA.unpack(u"\1\u01a0"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a1"),
        DFA.unpack(u"\1\u01a2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01a3"),
        DFA.unpack(u"\1\u01a4"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01a7"),
        DFA.unpack(u"\1\u01a8"),
        DFA.unpack(u"\1\u01a9"),
        DFA.unpack(u"\1\u01aa"),
        DFA.unpack(u"\1\u01ab"),
        DFA.unpack(u"\1\u01ac"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01ae"),
        DFA.unpack(u"\1\u01af"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01b2\20\uffff\1\u01b1"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01b4"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01b6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01b7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01b8"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01b9"),
        DFA.unpack(u"\1\u01ba"),
        DFA.unpack(u"\1\u01bb"),
        DFA.unpack(u"\1\u01bc"),
        DFA.unpack(u"\1\u01bd"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01be"),
        DFA.unpack(u"\1\u01bf"),
        DFA.unpack(u"\1\u01c0"),
        DFA.unpack(u"\1\u01c1"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01c2"),
        DFA.unpack(u"\1\u01c3"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01c5"),
        DFA.unpack(u"\1\u01c6"),
        DFA.unpack(u"\1\u01c7"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01cb"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01cd"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01cf"),
        DFA.unpack(u"\1\u01d0"),
        DFA.unpack(u"\1\u01d1"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01d3"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d4"),
        DFA.unpack(u"\1\u01d5"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01d8"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01d9"),
        DFA.unpack(u"\1\u01da"),
        DFA.unpack(u"\1\u01db"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01dd"),
        DFA.unpack(u"\1\u01de"),
        DFA.unpack(u"\1\u01df"),
        DFA.unpack(u"\1\u01e0"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01e2"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01e4"),
        DFA.unpack(u"\1\u01e5"),
        DFA.unpack(u"\1\u01e6"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01e8"),
        DFA.unpack(u"\1\u01e9"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01eb"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01ef"),
        DFA.unpack(u"\1\u01f0"),
        DFA.unpack(u"\1\u01f1"),
        DFA.unpack(u"\1\u01f2"),
        DFA.unpack(u"\1\u01f3"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01f6"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u01f7"),
        DFA.unpack(u"\1\u01f8"),
        DFA.unpack(u"\1\u01f9"),
        DFA.unpack(u"\1\u01fa"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01fc"),
        DFA.unpack(u"\1\u01fd"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u01ff"),
        DFA.unpack(u"\1\u0200"),
        DFA.unpack(u"\1\u0201"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0203"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0205"),
        DFA.unpack(u"\1\u0206"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0208"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u020b"),
        DFA.unpack(u"\1\u020c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u020d"),
        DFA.unpack(u"\1\u020e"),
        DFA.unpack(u"\1\u020f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0212"),
        DFA.unpack(u"\1\u0213"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0214"),
        DFA.unpack(u"\1\u0215"),
        DFA.unpack(u"\1\u0216"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0218"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\10\27\1\u021a\21\27\4"
        u"\uffff\1\27"),
        DFA.unpack(u"\1\u021c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u021d"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u021f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0224"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0226\1\uffff\1\u0227\2\uffff\1\u0228"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u022a"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u022d"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0231"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0232"),
        DFA.unpack(u"\1\u0233"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0234"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0236"),
        DFA.unpack(u"\1\u0237"),
        DFA.unpack(u"\1\u0238"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u023b"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u023d"),
        DFA.unpack(u"\1\u023e"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u023f"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0240"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0241"),
        DFA.unpack(u"\1\u0242"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0243"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\2\27\1\u0244\7\27\7\uffff\32\27\4\uffff"
        u"\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0246"),
        DFA.unpack(u"\1\u0247"),
        DFA.unpack(u"\1\u0248"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0249"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u024c"),
        DFA.unpack(u"\1\u024d"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u024f"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\2\27\1\u0252\7\27\7\uffff\32\27\4\uffff"
        u"\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0254"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0256"),
        DFA.unpack(u"\1\u0257"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0259"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u025c"),
        DFA.unpack(u"\1\u025d"),
        DFA.unpack(u"\1\u025e"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0264"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0268"),
        DFA.unpack(u"\1\u0269"),
        DFA.unpack(u"\1\u026a"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u026b"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u026c"),
        DFA.unpack(u"\1\u026d"),
        DFA.unpack(u"\1\u026e"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0270"),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"\1\u0272"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0274"),
        DFA.unpack(u""),
        DFA.unpack(u"\2\27\13\uffff\12\27\7\uffff\32\27\4\uffff\1\27"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA14_22 = input.LA(1)

                s = -1
                if ((0 <= LA14_22 <= 65535)):
                    s = 21

                else:
                    s = 116

                if s >= 0:
                    return s

            if self._state.backtracking > 0:
                raise BacktrackingFailed

            nvae = NoViableAltException(self_.getDescription(), 14, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(PLSQL3Lexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
