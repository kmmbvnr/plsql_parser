#!/usr/bin/env python
# -*- coding: utf-8 -*-

KEYWORDS = [x for x in '''

ACCESS
ADD
ALL
ALTER
AND
ANY
AS
ASC
AUDIT
BETWEEN
BY
CHAR
CHECK
CLUSTER
COLUMN
COLUMN_VALUE (See Note 1 at the end of this list)
COMMENT
COMPRESS
CONNECT
CREATE
CURRENT
DATE
DECIMAL
DEFAULT
DELETE
DESC
DISTINCT
DROP
ELSE
EXCLUSIVE
EXISTS
FILE
FLOAT
FOR
FROM
GRANT
GROUP
HAVING
IDENTIFIED
IMMEDIATE
IN
INCREMENT
INDEX
INITIAL
INSERT
INTEGER
INTERSECT
INTO
IS
LEVEL
LIKE
LOCK
LONG
MAXEXTENTS
MINUS
MLSLABEL
MODE
MODIFY
NESTED_TABLE_ID (See Note 1 at the end of this list)
NOAUDIT
NOCOMPRESS
NOT
NOWAIT
NULL
NUMBER
OF
OFFLINE
ON
ONLINE
OPTION
OR
ORDER
PCTFREE
PRIOR
PRIVILEGES
PUBLIC
RAW
RENAME
RESOURCE
REVOKE
ROW
ROWID (See Note 2 at the end of this list)
ROWNUM
ROWS
SELECT
SESSION
SET
SHARE
SIZE
SMALLINT
START
SUCCESSFUL
SYNONYM
SYSDATE
TABLE
THEN
TO
TRIGGER
UID
UNION
UNIQUE
UPDATE
USER
VALIDATE
VALUES
VARCHAR
VARCHAR2
VIEW
WHENEVER
WHERE
WITH
'''.split() if x]

from pyparsing import *

def KW(text):
    return CaselessKeyword(text)

EOS = Literal(';')
name = Word('a-zA-Z_#', 'a-zA-Z0-9_#', max=30)
label = name
variable = name

expression = Forward()

'''placeholder_expression =
:host_variable[:indicator_variable];'''
indicator_variable = variable
host_variable = ':' + variable
placeholder = placeholder_expression = host_variable + Optional(
    ':' + indicator_variable)


function_call = name
index = collection = name
named_cursor = name
constant = variable

numeric_constant = constant
numeric_variable = variable
numeric_literal = nums + Optional('.' + nums)
numeric_function_call = function_call
exponent = numeric_literal
'''
numeric_subexpression =
 { collection . { COUNT
                | FIRST
                | LAST
                | LIMIT
                | { NEXT | PRIOR } ( index )
                }
 | named_cursor%ROWCOUNT
 | numeric_constant
 | numeric_function_call
 | numeric_literal
 | numeric_variable
 | placeholder
 | SQL%{ROWCOUNT | BULK_ROWCOUNT ( index )}
 }
 [ ** exponent ];'''
numeric_subexpression = (
    (collection + '.'
        + (KW('COUNT') | KW('FIRST') | KW('LAST') | KW('LIMIT')
          | ((KW('NEXT') | KW('PRIOR')) + '(' + index + ')')))
    | (named_cursor + '%' + KW('ROWCOUNT'))
    | numeric_constant
    | numeric_function_call
    | numeric_literal
    | numeric_variable
    | placeholder
    | (KW('SQL') + '%'
      + (KW('ROWCOUNT') | (KW('BULK_ROWCOUNT') + '(' + index + ')')))
    ) + Optional('**' + exponent)

'''numeric_expression =
 numeric_subexpression
 [ { + | - | * | / } numeric_subexpression ]...;'''
numeric_expression = numeric_subexpression + ZeroOrMore((Literal('+') | '-' | '*' | '/') + numeric_subexpression)

character_literal = Combine("'" + ZeroOrMore("''" | CharsNotIn("'")) + "'")
date_constant = constant
date_function_call = function_call
date_literal = character_literal
date_variable = variable
'''date_expression =
{ date_constant
| date_function_call
| date_literal
| date_variable
| placeholder]
}
  [ { + | - } numeric_expression ] [ { + | - } numeric_expression ] ]...;'''
date_expression = (date_constant | date_function_call
    | date_literal | date_variable
    | placeholder) + ZeroOrMore((Literal('+') | '-') + numeric_expression)

_type = name
collection_type = _type
value = expression
'''collection_constructor =
collection_type ( [ value [, value]... ]);'''
collection_constructor = collection_type + '(' + Optional(value + ZeroOrMore(',' + value)) + ')'

character_function_call = function_call
character_constant = constant
character_variable = variable

'''character_expression =
 { character_constant
   | character_function_call
   | character_literal
   | character_variable
   | placeholder]
 }
 [|| { character_constant
       | character_function_call
       | character_literal
       | character_variable
       | placeholder]
      }
 [|| { character_constant
       | character_function_call
       | character_literal
       | character_variable
       | placeholder]
     } ]...;'''
character_expr = (
    character_constant
    | character_function_call
    | character_literal
    | character_variable
    | placeholder)
character_expression = character_expr + ZeroOrMore('||' + character_expr)

'''other_boolean_form =
{ collection.EXISTS ( index )
| expression { IS [ NOT ] NULL
             | [ NOT ] { BETWEEN expression AND expression
                       | IN ( expression [, expression ]... )
                       | LIKE pattern
                       }
             | relational_operator expression
             }
| { named_cursor | SQL } % { FOUND | ISOPEN | NOTFOUND }
};'''
boolean_variable = variable
boolean_function_call = function_call
boolean_constant = constant
relational_operator = (Literal('<') | '>' | '=' | '<=' | '>=' | '<>')
pattern = character_literal
other_boolean_form = (
    (collection + '.' + KW('EXISTS') + '(' + index + ')')
    | (expression + ((KW('IS') + Optional(KW('NOT')) + KW('NULL'))
                    | (Optional(KW('NOT'))
                       + ((KW('BETWEEN') + expression + KW('AND') + expression)
                          | (KW('IN') + '(' + expression + ZeroOrMore(',' + expression))
                          | (KW('LIKE') + pattern)
                          ))
                    | (relational_operator + expression)
                    ))
    | ((named_cursor | KW('SQL')) + '%' + (KW('FOUND') | KW('ISOPEN') | KW('NOTFOUND')))
    )

'''conditional_predicate =
 { INSERTING | UPDATING [ ( 'column' ) ] | DELETING };'''
conditional_predicate = (KW('INSERTING')
    | (KW('UPDATING') + Optional('(' + "'" + name + "'" + ')'))
    | KW('DELETING'))

'''boolean_literal =
 { TRUE | FALSE | NULL };'''
boolean_literal = KW('TRUE') | KW('FALSE') + KW('NULL')

'''boolean_expression =
[ NOT ] { boolean_constant
        | boolean_function_call
        | boolean_literal
        | boolean_variable
        | conditional_predicate
        | other_boolean_form
        }
        [ { AND | OR } [ NOT ] { boolean_constant
                               | boolean_function_call
                               | boolean_literal
                               | boolean_variable
                               | conditional_predicate
                               | other_boolean_form
                               }
        ]...;'''
boolean_expr = (Optional(KW('NOT'))
    + ( boolean_constant
        | boolean_function_call
        | boolean_literal
        | boolean_variable
        | conditional_predicate
        | other_boolean_form
        ))
boolean_expression = boolean_expr + ZeroOrMore((KW('AND') | KW('OR')) + boolean_expr)

'''simple_case_expression =
CASE case_operand
  WHEN case_operand_value THEN result_value
[ WHEN case_operand_value THEN result_value]...
[ ELSE result_value]
END;'''
case_operand = variable
case_operand_value = value
result_value = value
simple_case_expression = (KW('CASE') + case_operand
    + OneOrMore(KW('WHEN') + case_operand_value + KW('THEN')
                + result_value)
    + Optional(KW('ELSE') + result_value) + KW('END'))

'''searched_case_expression =
CASE
  WHEN boolean_expression THEN result_value
[ WHEN boolean_expression THEN result_value]...
[ ELSE result_value]
END;'''
searched_case_expression = (KW('CASE')
    + OneOrMore(KW('WHEN') + boolean_expression + KW('THEN')
                + result_value)
    + Optional(KW('ELSE') + result_value) + KW('END'))

'''expression =
 { boolean_expression
   | character_expression
   | collection_constructor
   | date_expression
   | numeric_expression
   | searched_case_expression
   | simple_case_expression
   | ( expression )
   };'''
expression << (
   boolean_expression
   | character_expression
   | collection_constructor
   | date_expression
   | numeric_expression
   | searched_case_expression
   | simple_case_expression
   | (Literal('(') + expression + Literal(')'))
   )

'''exit_statement =
EXIT [ label ] [ WHEN boolean_expression ]  EOS;
'''
exit_statement = KW('EXIT') + Optional(label) + Optional(KW('WHEN') + boolean_expression) + EOS

collection_variable = cursor_variable = db_table_or_view = object_ = record_variable = scalar_variable = name

'''type_attribute =
{ collection_variable
| cursor_variable
| db_table_or_view.column
| object
| record_variable[.field ]
| scalar_variable
}
  %TYPE;'''
type_attribute = (
  collection_variable
| cursor_variable
| (db_table_or_view + '.' + name)
| object_
| (record_variable + Optional('.' + name))
| scalar_variable
) + '%' + KW('TYPE')

'''
rowtype =
{ {db_table_or_view | cursor | cursor_variable}%ROWTYPE
  | record%TYPE
  | record_type
  };'''
record = name
record_type = _type

'''rowtype_attribute =
{ explicit_cursor | cursor_variable | db_table_or_view } %ROWTYPE;
'''
explicit_cursor = variable
rowtype_attribute = ((explicit_cursor | cursor_variable | db_table_or_view) + '%' + KW('ROWTYPE'))

''' datatype =
 { collection_type
 | [ REF ] object_type
 | record_type
 | ref_cursor_type
 | rowtype_attribute
 | scalar_datatype
 | type_attribute
 };'''
object_type = name
ref_cursor_type = KW('SYS_REFCURSOR') | _type
scalar_datatype = (KW('PLS_INTEGER') | KW('BINARY_INTEGER') | KW('BOOLEAN')
    | ((KW('CHAR') | KW('VARCHAR2')) + '(' + nums + ')')
    | (KW('INTEGER') + Optional('(' + nums + ')'))
    | (KW('NUMBER') + Optional('(' + nums + Optional(',' + nums) + ')'))
    )
datatype = (collection_type | (Optional(KW('REF')) + object_type)
    | record_type | ref_cursor_type | rowtype_attribute
    | scalar_datatype | type_attribute)

rowtype = (
    (db_table_or_view | named_cursor | cursor_variable) + '%' + KW('ROWTYPE')
    | (record + '%' + KW('TYPE'))
    | record_type)

'''cursor_parameter_dec =
parameter [IN] datatype [ { := | DEFAULT } expression ];
'''
cursor_parameter_dec = name + Optional(KW('IN')) + datatype + Optional((':=' | KW('DEFAULT')) + expression)

cursor_parameter_declaration = cursor_parameter_dec + ZeroOrMore(',' + cursor_parameter_dec)

cursor_definition_head = (KW('CURSOR') + name
    + Optional('(' + OneOrMore(cursor_parameter_declaration) + ')'))

select_statement = KW('SELECT')  # + SkipTo(EOS + LineEnd)
'''cursor_definition =
CURSOR cursor
 [ ( cursor_parameter_declaration [, cursor_parameter_declaration ]... )]
   [ RETURN rowtype] IS select_statement  EOS;
'''
cursor_definition = (cursor_definition_head
    + Optional(KW('RETURN') + rowtype)
    + KW('IS') + select_statement + EOS)

'''cursor_declaration =
CURSOR cursor
  [( cursor_parameter_declaration [, cursor_parameter_declaration ]... )]
    RETURN rowtype EOS;
'''
cursor_declaration = cursor_definition_head + KW('RETURN') + rowtype + EOS

'''goto_statement =
GOTO label  EOS;
'''
goto_statement = KW('GOTO') + label + EOS

'''continue_statement =
CONTINUE [ label ] [ WHEN boolean_expression ]  EOS;
'''
continue_statement = KW('CONTINUE') + Optional(label) + Optional(KW('WHEN') + boolean_expression) + EOS

'''where_clause =
WHERE condition CURRENT OF for_update_cursor;
'''
condition = SkipTo(KW('CURRENT') + KW('OF'))
for_update_cursor = variable
where_clause = KW('WHERE') + condition + KW('CURRENT') + KW('OF') + for_update_cursor

'''update_set_clause =
SET ROW record;'''
update_set_clause = KW('SET') + KW('ROW') + record

'''relies_on_clause =
RELIES_ON ( [ data_source [, data_source]... ] );'''
data_source = db_table_or_view
relies_on_clause = KW('RELIES_ON') + '(' + Optional(data_source + ZeroOrMore(',' + data_source)) + ')'

'''variable_declaration =
variable datatype [ [ NOT NULL] {:= | DEFAULT} expression ]  EOS;'''
variable_declaration = (variable + datatype
    + Optional(Optional(KW('NOT') + KW('NULL'))
               + (Literal(':=') | KW('DEFAULT'))
               + expression)
    + EOS)

'''close_statement =
CLOSE { cursor | cursor_variable | :host_cursor_variable }  EOS;'''
close_statement = KW('CLOSE') + named_cursor | cursor_variable | (
    (':' + host_variable))

'''assignment_statement_target =
{ collection_variable [ ( index ) ]
| cursor_variable
| :host_cursor_variable
| object[.attribute]
| out_parameter
| placeholder
| record_variable[.field]
| scalar_variable
};'''
assignment_statement_target = (
  (collection_variable + Optional('(' + index + ')'))
| cursor_variable
| host_variable
| (object_ + Optional('.' + name))
| variable
| placeholder
| (record_variable + Optional('.' + name))
| scalar_variable)

'''assignment_statement =
assignment_statement_target := expression  EOS;'''
assignment_statement = assignment_statement_target + ':=' + expression + EOS

'''parameter_declaration =
parameter [ [ IN ] datatype [ { := | DEFAULT } expression ]
          | { OUT | IN OUT } [ NOCOPY ] datatype;'''
parameter_dec = name + Optional(
    ((KW('IN') + Optional((':=' | KW('DEFAULT')) + expression))
    | ((KW('OUT') | (KW('IN') + KW('OUT'))) + Optional(KW('NOCOPY')))
    )) + datatype

parameter_declaration = parameter_dec + ZeroOrMore(',' + parameter_dec)

'''function_heading =
FUNCTION function [ ( parameter_declaration [, parameter_declaration ] ) ]
  RETURN datatype;'''
function_heading = KW('FUNCTION') + name + Optional('(' + parameter_declaration + ZeroOrMore(',' + parameter_declaration) + ')') + KW('RETURN') + datatype

'''function_definition =
function_heading [ DETERMINISTIC
                 | PIPELINED
                 | PARALLEL_ENABLE
                 | RESULT_CACHE [ relies_on_clause ]
                 ]...
  { IS | AS } { [ declare_section ] body | call_spec | EXTERNAL };'''
function_definition = function_heading + ZeroOrMore(
    KW('DETERMINISTIC')
  | KW('PIPELINED') | KW('PARALLEL_ENABLE')
  | (KW('RESULT_CACHE') + Optional(relies_on_clause))) + (KW('IS') | KW('AS')) + ((Optional(declare_section) + body)
            | call_spec | KW('EXTERNAL'))

'''function_declaration =
function_heading
  [ DETERMINISTIC | PIPELINED | PARALLEL_ENABLE | RESULT_CACHE ]...  EOS;'''
function_declaration = (function_heading + ZeroOrMore(*map(KW,
    'DETERMINISTIC PIPELINED PARALLEL_ENABLE RESULT_CACHE'.split()))
    + EOS)


'''
function_call =
function [ ( [ parameter [, parameter ]... ] ) ];'''
function_call = name + Optional('(' + Optional(parameter + ZeroOrMore(',' + parameter)) + ')')

'''open_statement =
OPEN cursor [ ( cursor_parameter [ [,] actual_cursor_parameter ]... ) ]  EOS;'''
open_statement = KW('OPEN') + named_cursor + Optional('(' + parameter + ZeroOrMore(',' + parameter) + ')')

'''exception_declaration =
exception EXCEPTION EOS;'''
exception_declaration = name + KW('EXCEPTION') + EOS

'''cursor_variable_declaration =
cursor_variable type EOS;

ref_cursor_type_definition =
TYPE type IS REF CURSOR
  [ RETURN
    { {db_table_or_view | cursor | cursor_variable}%ROWTYPE
    | record%TYPE
    | record_type
    | ref_cursor_type
    }
  ]  EOS;

raise_statement =
RAISE [ exception ]  EOS;

while_loop_statement =
WHILE boolean_expression
  LOOP statement... END LOOP [ label ]  EOS;

return_statement =
RETURN [ expression ]  EOS;

pipe_row_statement =
PIPE ROW ( row )  EOS;

if_statement =
IF boolean_expression THEN statement [ statement ]...
 [ ELSIF boolean_expression THEN statement [ statement ]... ]...
   [ ELSE statement [ statement ]... ] END IF  EOS;

null_statement =
NULL  EOS;

collection_variable_dec =
new_collection_var
   { assoc_array_type
   | { varray_type | nested_table_type }
       [ :=  { collection_constructor | collection_var_1 }
   | collection_var_2%TYPE
   }  EOS;


nested_table_type_def =
TABLE OF datatype [ NOT NULL ];

varray_type_def =
{ VARRAY | VARYING ARRAY } ( size_limit )
  OF datatype [ NOT NULL ];

assoc_array_type_def =
TABLE OF datatype [ NOT NULL ]
INDEX BY { PLS_INTEGER | BINARY_INTEGER | VARCHAR2 ( v_size ) | data_type };

collection_type_def =
TYPE type IS
   { assoc_array_type_def
   | varray_type_def
   | nested_table_type_def
   }  EOS;

basic_loop_statement =
LOOP statement... END LOOP [ label ]  EOS;'''

'''fetch_statement =
FETCH { cursor | cursor_variable | :host_cursor_variable }
  { into_clause | bulk_collect_into_clause [ LIMIT numeric_expression ] }  EOS;

values_clause =
VALUES record;

insert_into_clause =
INTO dml_expression_clause [ t_alias ];

bounds_clause =
{ lower_bound .. upper_bound
| INDICES OF collection [ BETWEEN lower_bound AND upper_bound ]
| VALUES OF index_collection
};

forall_statement =
FORALL index IN bounds_clause [ SAVE EXCEPTIONS ] dml_statement EOS;

for_loop_statement =
[ FOR index IN [ REVERSE ] lower_bound .. upper_bound
    LOOP statement... END LOOP [ label ]  EOS;

cursor_for_loop_statement =
[ FOR record IN
  { cursor [ ( cursor_parameter_declaration
               [ [,] cursor_parameter_declaration ]... )]
  | ( select_statement )
  }
    LOOP statement... END LOOP [label]  EOS;

inline_pragma =
PRAGMA INLINE ( subprogram , { 'YES' | 'NO' } )  EOS;

exception_handler =
WHEN { exception [ OR exception ]... | OTHERS }
  THEN statement [ statement ]...;

procedure_definition =
procedure_heading { IS | AS }
  { [ declare_section ] body | call_spec | EXTERNAL };

procedure_heading =
PROCEDURE procedure [ ( parameter_declaration [, parameter_declaration ]... ) ];

procedure_declaration =
procedure_heading;

sql_statement =
{ commit_statement
| delete_statement
| insert_statement
| lock_table_statement
| rollback_statement
| savepoint_statement
| set_transaction_statement
| update_statement
};

procedure_call =
procedure [ ( [ parameter [, parameter ]... ] ) ]  EOS;

statement =
[ "<<" label ">>" [ "<<" label ">>" ] ...]
  { assignment_statement
  | basic_loop_statement
  | close_statement
  | continue_statement
  | cursor_for_loop_statement
  | execute_immediate_statement
  | exit_statement
  | fetch_statement
  | for_loop_statement
  | forall_statement
  | goto_statement
  | if_statement
  | null_statement
  | open_statement
  | open_for_statement
  | pipe_row_statement
  | plsql_block
  | raise_statement
  | return_statement
  | select_into_statement
  | sql_statement
  | while_loop_statement
  };

basic_body =
BEGIN statement [ statement | inline_pragma ]...
  [ EXCEPTION exception_handler [ exception_handler ]... ] END [ name ]  EOS;

pragma =
{ autonomous_transaction_pragma
| exception_init_pragma
| inline_pragma
| restrict_references_pragma
| serially_reusable_pragma
};

item_declaration =
{ collection_variable_dec
| constant_declaration
| cursor_variable_declaration
| exception_declaration
| record_variable_declaration
| variable_declaration
};

constraint =
{ precision [, scale ] | RANGE low_value .. high_value };

subtype_definition =
SUBTYPE subtype IS base_type [ constraint | CHARACTER SET character_set ]
  [ NOT NULL ];

type_definition =
{ collection_type_definition
| record_type_definition
| ref_cursor_type_definition
| subtype_definition
};

item_list_2 =
{ cursor_declaration
| cursor_definition
| function_declaration
| function_definition
| procedure_declaration
| procedure_definition
}
  [ { cursor_declaration
    | cursor_definition
    | function_declaration
    | function_definition
    | procedure_declaration
    | procedure_definition
    | pragma
    }
  ]...;

item_list_1 =
{ type_definition
| cursor_declaration
| item_declaration
| function_declaration
| procedure_declaration
}
  [ { type_definition
    | cursor_declaration
    | item_declaration
    | function_declaration
    | procedure_declaration
    | pragma
    }
  ]...;

declare_section =
{ item_list_1 [ item_list_2 ] | item_list_2 };

plsql_block =
[ "<<" label ">>" ]... [ DECLARE declare_section ] body;

initialize_section =
BEGIN statement [ statement | pragma ]...
  [ EXCEPTION exception_handler [ exception_handler ]... ];

create_package_body =
CREATE [ OR REPLACE ] PACKAGE BODY [ schema. ] package_name
{ IS | AS } declare_section [ initialize_section ]
END [ package_name ]  EOS;

invoker_rights_clause =
AUTHID { CURRENT_USER | DEFINER };

create_package =
CREATE [ OR REPLACE ] PACKAGE [ schema. ] package_name
   [ invoker_rights_clause ]
   { IS | AS } declare_section END [ package_name ]  EOS;
'''

'''
statement =
[ "<<" label ">>" [ "<<" label ">>" ] ...]
  { assignment_statement
  | basic_loop_statement
  | close_statement
  | continue_statement
  | cursor_for_loop_statement
  | execute_immediate_statement
  | exit_statement
  | fetch_statement
  | for_loop_statement
  | forall_statement
  | goto_statement
  | if_statement
  | null_statement
  | open_statement
  | open_for_statement
  | pipe_row_statement
  | plsql_block
  | raise_statement
  | return_statement
  | select_into_statement
  | sql_statement
  | while_loop_statement
  };'''
statement = ZeroOrMore("<<" + name + ">>") + (
    assignment_statement
  | basic_loop_statement
  | close_statement
  | continue_statement
  | cursor_for_loop_statement
  | execute_immediate_statement
  | exit_statement
  | fetch_statement
  | for_loop_statement
  | forall_statement
  | goto_statement
  | if_statement
  | null_statement
  | open_statement
  | open_for_statement
  | pipe_row_statement
  | plsql_block
  | raise_statement
  | return_statement
  | select_into_statement
  | sql_statement
  | while_loop_statement) + EOS

'''exception_handler =
WHEN { exception [ OR exception ]... | OTHERS }
  THEN statement [ statement ]...;'''
exception_handler = KW('WHEN') + (name + ZeroOrMany(Optional(KW('OR') + name)) | KW('OTHERS')) + KW('THEN') + statement

'''initialize_section =
BEGIN statement [ statement | pragma ]...
  [ EXCEPTION exception_handler [ exception_handler ]... ];'''
initialize_section = KW('BEGIN') + statement + ZeroOrMany(statement | pragma) + Optional(KW('EXCEPTION') + OneOrMany(exception_handler))

'''
plsql_block =
[ "<<" label ">>" ]... [ DECLARE declare_section ] body;
declare_section =
{ item_list_1 [ item_list_2 ] | item_list_2 };
item_list_1 =
{ type_definition
| cursor_declaration
| item_declaration
| function_declaration
| procedure_declaration
}
  [ { type_definition
    | cursor_declaration
    | item_declaration
    | function_declaration
    | procedure_declaration
    | pragma
    }
  ]...;
item_list_2 =
{ cursor_declaration
| cursor_definition
| function_declaration
| function_definition
| procedure_declaration
| procedure_definition
}
  [ { cursor_declaration
    | cursor_definition
    | function_declaration
    | function_definition
    | procedure_declaration
    | procedure_definition
    | pragma
    }
  ]...;
type_definition =
{ collection_type_definition
| record_type_definition
| ref_cursor_type_definition
| subtype_definition
};
subtype_definition =
SUBTYPE subtype IS base_type [ constraint | CHARACTER SET character_set ]
  [ NOT NULL ];
constraint =
{ precision [, scale ] | RANGE low_value .. high_value };
item_declaration =
{ collection_variable_dec
| constant_declaration
| cursor_variable_declaration
| exception_declaration
| record_variable_declaration
| variable_declaration
};
pragma =
{ autonomous_transaction_pragma
| exception_init_pragma
| inline_pragma
| restrict_references_pragma
| serially_reusable_pragma
};
basic_body =
BEGIN statement [ statement | inline_pragma ]...
  [ EXCEPTION exception_handler [ exception_handler ]... ] END [ name ]  EOS;
'''

'''invoker_rights_clause =
AUTHID { CURRENT_USER | DEFINER };'''
invoker_rights_clause = KW('AUTHID') + (KW('CURRENT_USER') | KW('DEFINER')) + EOS
'''create_package =
CREATE [ OR REPLACE ] PACKAGE [ schema. ] package_name
   [ invoker_rights_clause ]
   { IS | AS } declare_section END [ package_name ]  EOS;
   '''
create_package = KW('CREATE') + Optional(KW('OR') + KW('REPLACE')) + KW('PACKAGE') + Optional(name + '.') + name + invoker_rights_clause + (KW('IS') | KW('AS')) + declare_section + KW('END') + EOS

'''
create_package_body =
CREATE [ OR REPLACE ] PACKAGE BODY [ schema. ] package_name
{ IS | AS } declare_section [ initialize_section ]
END [ package_name ]  EOS;
'''
