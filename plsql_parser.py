#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyparsing import *


def KW(text):
    return CaselessKeyword(text)


def kw(text):
    return And(map(KW, text.upper().split()))


def sepmul(tok, sep=','):
    return (tok + ZeroOrMore(sep + tok))


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

character_literal = QuotedString("'", escQuote="''", multiline=True)
# Combine("'" + ZeroOrMore("''" | CharsNotIn("'")) + "'")
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
comma_exprs = sepmul(expression, ',')
comma_values = sepmul(value, ',')
comma_names = sepmul(name, ',')
'''collection_constructor =
collection_type ( [ value [, value]... ]);'''
collection_constructor = collection_type + '(' + Optional(comma_values) + ')'

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
                          | (KW('IN') + '(' + comma_exprs + ')')
                          | (KW('LIKE') + pattern))
                          )
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
boolean_literal = KW('TRUE') | kw('FALSE NULL')

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

cursor_parameter_declaration = sepmul(cursor_parameter_dec, ',')

cursor_definition_head = (KW('CURSOR') + name
    + Optional('(' + OneOrMore(cursor_parameter_declaration) + ')'))

select_statement = KW('SELECT') + SkipTo(EOS & LineEnd())
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
condition = SkipTo(kw('CURRENT OF'))
for_update_cursor = variable
where_clause = KW('WHERE') + condition + kw('CURRENT OF') + for_update_cursor

'''update_set_clause =
SET ROW record;'''
update_set_clause = kw('SET ROW') + record

'''relies_on_clause =
RELIES_ON ( [ data_source [, data_source]... ] );'''
data_source = db_table_or_view
relies_on_clause = KW('RELIES_ON') + '(' + Optional(sepmul(data_source, ',')) + ')'

'''variable_declaration =
variable datatype [ [ NOT NULL] {:= | DEFAULT} expression ]  EOS;'''
variable_declaration = (variable + datatype
    + Optional(Optional(kw('NOT NULL'))
               + (Literal(':=') | KW('DEFAULT'))
               + expression)
    + EOS)

'''close_statement =
CLOSE { cursor | cursor_variable | :host_cursor_variable }  EOS;'''
close_statement = KW('CLOSE') + (named_cursor | cursor_variable | host_variable)

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

parameter_declaration = sepmul(parameter_dec, ',')

parameter = expression

'''
function_call =
function [ ( [ parameter [, parameter ]... ] ) ];'''
function_call = name + Optional('(' + Optional(sepmul(parameter, ',')) + ')')

'''open_statement =
OPEN cursor [ ( cursor_parameter [ [,] actual_cursor_parameter ]... ) ]  EOS;'''
open_statement = KW('OPEN') + named_cursor + Optional('(' + sepmul(parameter, ',') + ')')

'''exception_declaration =
exception EXCEPTION EOS;'''
exception_declaration = name + KW('EXCEPTION') + EOS

'''cursor_variable_declaration =
cursor_variable type EOS;'''
cursor_variable_declaration = cursor_variable + _type + EOS

'''ref_cursor_type_definition =
TYPE type IS REF CURSOR
  [ RETURN
    { {db_table_or_view | cursor | cursor_variable}%ROWTYPE
    | record%TYPE
    | record_type
    | ref_cursor_type
    }
  ]  EOS;'''
ref_cursor_type_definition = (KW('TYPE') + _type + kw('IS REF CURSOR')
    + Optional(
        (KW('RETURN') + ((db_table_or_view | named_cursor | cursor_variable) + '%' + KW('ROWTYPE')))
        | (record + '%' + KW('TYPE'))
        | record_type
        | ref_cursor_type)
    + EOS)


statement = Forward()

exception = name
'''raise_statement =
RAISE [ exception ]  EOS;'''
raise_statement = KW('RAISE') + Optional(exception) + EOS

'''while_loop_statement =
WHILE boolean_expression
  LOOP statement... END LOOP [ label ]  EOS;'''
while_loop_statement = (KW('WHILE') + boolean_expression + KW('LOOP')
    + OneOrMore(statement) + kw('END LOOP') + Optional(label) + EOS)

'''return_statement =
RETURN [ expression ]  EOS;'''
return_statement = KW('RETURN') + Optional(expression) + EOS

row = variable
'''pipe_row_statement =
PIPE ROW ( row )  EOS;'''
pipe_row_statement = kw('PIPE ROW') + '(' + row + ')' + EOS

'''if_statement =
IF boolean_expression THEN statement [ statement ]...
 [ ELSIF boolean_expression THEN statement [ statement ]... ]...
   [ ELSE statement [ statement ]... ] END IF  EOS;'''
if_statement = (KW('IF') + boolean_expression + KW('THEN') + OneOrMore(statement)
    + Optional(KW('ELSIF') + boolean_expression + KW('THEN') + OneOrMore(statement))
    + Optional(KW('ELSE') + OneOrMore(statement))
    + kw('END IF') + EOS)

'''null_statement =
NULL  EOS;'''
null_statement = KW('NULL') + EOS

'''collection_variable_dec =
new_collection_var
   { assoc_array_type
   | { varray_type | nested_table_type }
       [ :=  { collection_constructor | collection_var_1 }
   | collection_var_2%TYPE
   }  EOS;'''
assoc_array_type = _type
varray_type = _type
nested_table_type = _type
size_limit = nums
collection_variable_dec = (name + (assoc_array_type | ((varray_type | nested_table_type) + Optional(':=' + (collection_constructor | name)))))

'''nested_table_type_def =
TABLE OF datatype [ NOT NULL ];'''
nested_table_type_def = kw('TABLE OF') + datatype + Optional(kw('NOT NULL'))

'''varray_type_def =
{ VARRAY | VARYING ARRAY } ( size_limit )
  OF datatype [ NOT NULL ];'''
varray_type_def = ((KW('VARRAY') | (kw('VARYING ARRAY')))
    + '(' + size_limit + ')' + KW('OF') + datatype
    + Optional(kw('NOT NULL')))

'''assoc_array_type_def =
TABLE OF datatype [ NOT NULL ]
INDEX BY { PLS_INTEGER | BINARY_INTEGER | VARCHAR2 ( v_size ) | data_type };'''
assoc_array_type_def = (kw('TABLE OF') + datatype
    + Optional(kw('NOT NULL'))
    + kw('INDEX BY') + (KW('PLS_INTEGER') | KW('BINARY_INTEGER')
                       | (KW('VARCHAR2') + '(' + size_limit + ')') | _type))

'''collection_type_def =
TYPE type IS
   { assoc_array_type_def
   | varray_type_def
   | nested_table_type_def
   }  EOS;'''
collection_type_def = (KW('TYPE') + _type + KW('IS')
+ (assoc_array_type_def | varray_type_def | nested_table_type_def) + EOS)

'''basic_loop_statement =
LOOP statement... END LOOP [ label ]  EOS;'''
basic_loop_statement = (KW('LOOP') + OneOrMore(statement)
+ kw('END LOOP') + Optional(label) + EOS)

'''bulk_collect_into_clause = BULK COLLECT INTO { collection | :host_array }
  [, { collection | :host_array } ]...
'''
bulk_collect_into_clause = kw('bulk collect into') + sepmul((collection | host_variable), ',')

'''into_clause =
INTO { variable [, variable ]... | record )'''
into_clause = kw('into') + (sepmul(variable, ',') | record)

'''fetch_statement =
FETCH { cursor | cursor_variable | :host_cursor_variable }
  { into_clause | bulk_collect_into_clause [ LIMIT numeric_expression ] }  EOS;'''
fetch_statement = (KW('FETCH') + (named_cursor | cursor_variable | host_variable)
    + (into_clause | (bulk_collect_into_clause
                      + Optional(KW('LIMIT') + numeric_expression)))
    + EOS)

'''values_clause =
VALUES record;'''
values_clause = KW('VALUES') + record

'''partition_extension_clause =
{ PARTITION (partition)
| PARTITION FOR (partition_key_value [, partition_key_value]...)
| SUBPARTITION (subpartition)
| SUBPARTITION FOR (subpartition_key_value [, subpartition_key_value]...)
}'''
partition_extension_clause = (
    ((kw('subpartition') | kw('partition')) + '(' + name + ')')
    | ((kw('subpartition for') | kw('partition for'))
       + '(' + comma_names + ')')
)

dblink = '@' + name

'''subquery_restriction_clause =
WITH { READ ONLY
     | CHECK OPTION
     } [ CONSTRAINT constraint ]'''
subquery_restriction_clause = (kw('WITH') + (kw('read only') | kw('check option'))
    + Optional(kw('constraint') + name))

subquery = Forward()

'''subquery, a column, a function, or a collection constructor'''
collection_expression = (subquery | name)

'''table_collection_expression =
TABLE (collection_expression) [ (+) ]'''
table_collection_expression = (kw('TABLE') + '(' + collection_expression + ')'
                               + Optional('(+)'))

'''sample_clause =
SAMPLE [ BLOCK ]
       (sample_percent)
       [ SEED (seed_value) ]'''
sample_clause = kw('sample') + Optional(kw('block')) + '(' + nums + '%' + ')' + Optional(kw('seed') + '(' + nums + ')')

'''unpivot_in_clause =
IN
( { column | ( column [, column]... ) }
      [  AS { literal | ( literal [, literal]... ) } ]
        [, { column | ( column [, column]... ) }
          [  AS {literal | ( literal [, literal]... ) } ]
        ]...
)'''
name_or_namelist = ('(' + (name | '(' + sepmul(name, ',') + ')')+ ')')
unpivot_in_clause = sepmul(kw('IN') + name_or_namelist
    + Optional(kw('AS') + name_or_namelist))

'''pivot_in_clause =
IN ( { { { expr
         | ( expr [, expr]... )
         } [ [ AS] alias]
       }...
     | subquery
     | ANY [, ANY]...
     }
   )'''
pivot_in_clause = (kw('IN') + '('
    + ((name_or_namelist + Optional(Optional(kw('AS')) + name))
       | subquery | sepmul(kw('ANY'))) + ')')



'''pivot_for_clause =
FOR { column
    | ( column [, column]... )
    }'''
pivot_for_clause = kw('FOR') + name_or_namelist

table_reference = Forward()

'''pivot_clause =
table_reference PIVOT [ XML ]
  ( aggregate_function ( expr ) [[AS] alias ]
      [, aggregate_function ( expr ) [[AS] alias ] ]...
    pivot_for_clause
    pivot_in_clause
  )'''
aggregate_function = name
pivot_clause = table_reference + kw('PIVOT') + Optional(kw('XML')) + ('('
    + aggregate_function + '(' + name + ')'
    + sepmul(Optional(Optional(kw('AS')) + name), ',')
    + pivot_for_clause + pivot_in_clause
    + ')')

'''unpivot_clause =
table_reference UNPIVOT [ {INCLUDE | EXCLUDE} NULLS ]
( { column | ( column [, column]... ) }
  pivot_for_clause
  unpivot_in_clause
)'''
unpivot_clause = (table_reference + kw('UNPIVOT')
    + Optional((kw('include') | kw('exclude')) + kw('nulls'))
    + '(' + (name | sepmul(name, ',')) + ')'
    + pivot_for_clause + unpivot_in_clause)

'''query_table_expression =
{ query_name
| [ schema. ]
  { table [ partition_extension_clause
          | @ dblink
          ]
  | { view | materialized view } [ @ dblink ]
  } ["sample_clause"]
| (subquery [ subquery_restriction_clause ])
| table_collection_expression
}'''
query_table_expression = (name
    | (Optional(name + '.')
       + ((name + Optional(partition_extension_clause | dblink))
          | (name + Optional(dblink)))
       + Optional(sample_clause))
    | ('(' + subquery + Optional(subquery_restriction_clause) + ')')
    | table_collection_expression)

alias = name
'''flashback_query_clause =
{ VERSIONS BETWEEN
  { SCN | TIMESTAMP }
  { expr | MINVALUE } AND { expr | MAXVALUE }
| AS OF { SCN | TIMESTAMP } expr
}'''
flashback_query_clause = (
    (kw('versions between') + (kw('scn') | kw('timestamp'))
     + (name | kw('minvalue')) + kw('AND') + (kw('name') | kw('maxvalue')))
    | (kw('as of') + (kw('scn') | kw('timestamp') + name)))

'''table_reference =
{ ONLY (query_table_expression)
| query_table_expression [ pivot_clause | unpivot_clause ]
} [ flashback_query_clause ]
  [ t_alias ]'''
table_reference << ((kw('ONLY') + '(' + query_table_expression + ')')
    | (query_table_expression + Optional(pivot_clause | unpivot_clause))
    ) + Optional(flashback_query_clause) + Optional(alias)

'''inner_cross_join_clause =
{ [ INNER ] JOIN table_reference
    { ON condition
    | USING (column [, column ]...)
    }
| { CROSS
  | NATURAL [ INNER ]
  }
  JOIN table_reference
}'''
inner_cross_join_clause = (
    (Optional(kw('inner')) + kw('join')
     + table_reference + ((kw('on') + condition)
                          | (kw('using') + '(' + comma_names + ')')))
    | ((kw('cross') | (kw('natural') + Optional(kw('inner')))) + kw('join') + table_reference)
)

'''query_partition_clause =
PARTITION BY
  { expr[, expr ]...
  | ( expr[, expr ]... )
  }'''
query_partition_clause = kw('parition by') + comma_exprs

'''outer_join_type =
{ FULL | LEFT | RIGHT } [ OUTER ]'''
outer_join_type = (kw('full') | kw('left') | kw('right')) + Optional(kw('outer'))

'''outer_join_clause =
  [ query_partition_clause ]
{ outer_join_type JOIN
| NATURAL [ outer_join_type ] JOIN
}
table_reference [ query_partition_clause ]
  [ ON condition
  | USING ( column [, column ]...)
  ]'''
outer_join_clause = (Optional(query_partition_clause) + (
    (outer_join_type + kw('JOIN'))
    | (kw('NATURAL') + Optional(outer_join_type) + kw('JOIN'))
    ) + table_reference + Optional(query_partition_clause)
    + Optional((kw('ON') + condition)
               | (kw('USING') + '(' + comma_names + ')')))

'''hint =
{ /*+ hint [ string ] [ hint [ string ] ]... */
| --+ hint [ string ] [ hint [ string ] ]...
}'''
hint = ((Literal('/*+') + SkipTo(Literal('*/'))) | Literal('--+') + SkipTo(LineEnd()))

'''join_clause =
table_reference
  { inner_cross_join_clause | outer_join_clause }...'''
join_clause = table_reference + OneOrMore(inner_cross_join_clause | outer_join_clause)

'''select_list ={ [t_alias.] *
| { query_name.*
  | [ schema. ]
    { table | view | materialized view } .*
  | expr [ [ AS ] c_alias ]
  }
    [, { query_name.*
       | [ schema. ]
         { table | view | materialized view } .*
       | expr [ [ AS ] c_alias ]
       }
    ]...
}'''
select_list = (
    (Optional(alias + '.') + '*')
    | sepmul((name + '.*')
             | (Optional(name + '.') + db_table_or_view + '.*')
             | (name + Optional(Optional(kw('AS')) + name)), ',')
)

'''hierarchical_query_clause =
{ CONNECT BY [ NOCYCLE ] condition [AND condition]... [ START WITH condition ]
| START WITH condition CONNECT BY [ NOCYCLE ] condition [AND condition]...
}'''
hierarchical_query_clause = (
    (kw('connect by') + Optional(kw('nocycle')) + sepmul(condition, kw('and')) + Optional(kw('start with') + condition))
    | (kw('start with') + condition + kw('connect by') + Optional(kw('nocycle')) + sepmul(condition, kw('AND'))))

'''group_by_clause =
'''

'''cell_reference_options =
[ { IGNORE | KEEP } NAV ]
[ UNIQUE { DIMENSION | SINGLE REFERENCE } ]'''
cell_reference_options = (
    Optional((kw('ignore') | kw('keep')) + kw('nav'))
    + Optional(kw('unique') + (kw('dimension') | kw('single reference'))))

'''return_rows_clause =
RETURN { UPDATED | ALL } ROWS'''
return_rows_clause = kw('return') + (kw('updated') | kw('all')) + kw('rows')

'''model_column =
expr [ [ AS ] c_alias ]'''
model_column = expression + Optional(Optional(kw('AS')) + name)

'''model_column_clauses =
[ PARTITION BY expr [ c_alias ] [, expr [c_alias] ]...
DIMENSION BY (expr [c_alias] [, expr [c_alias] ]...)
MEASURES (expr [c_alias] [, expr [c_alias] ]...)'''
expr_alias_list = sepmul(expression + Optional(name), ',')
model_column_clauses = (
    Optional(kw('partition by') + expr_alias_list)
    + kw('dimension by') + '(' + expr_alias_list + ')'
    + kw('measures') + '(' + expr_alias_list + ')')

'''model_iterate_clause =
ITERATE ( number ) [ UNTIL ( condition ) ]'''
model_iterate_clause = kw('iterate') + '(' + nums + ')' + Optional(
    kw('until') + '(' + condition + ')')

'''single_column_for_loop =
FOR dimension_column
  { IN ( { literal [, literal ]...
         | subquery
         }
       )
  | [ LIKE pattern ] FROM literal TO literal
      { INCREMENT | DECREMENT } literal
  }'''
literal = name
single_column_for_loop = (
    kw('for') + name + (
        (kw('in') + '(' + (sepmul(literal, ',') | subquery) + ')')
        | (Optional(kw('like') + pattern) + kw('from') + literal + kw('to') + literal
           + (kw('increment') | kw('decrement')) + literal)
        )
    )

'''multi_column_for_loop =
FOR (dimension_column
      [, dimension_column ]...)
IN ( { (literal [, literal ]...)
       [ (literal [, literal ]...) ]...
     | subquery
     }
   )'''
multi_column_for_loop = (
    kw('for') + '(' + sepmul(name, ',') + ')'
    + kw('in') + '(' + (sepmul(literal, ',') | subquery) + ')')

'''cell_assignment =
measure_column [ { { condition
                   | expr
                   | single_column_for_loop
                   }
                     [, { condition
                        | expr
                        | single_column_for_loop
                        }
                     ]...
                 | multi_column_for_loop
                 }
               ]

Note: The outer square brackets are part of the syntax.
      In this case, they do not indicate optionality.'''
cell_assignment = (name + '[' + (
        sepmul(condition | expression | single_column_for_loop, ',')
        | multi_column_for_loop) + ']')

'''order_by_clause =
ORDER [ SIBLINGS ] BY
{ expr | position | c_alias }
[ ASC | DESC ]
[ NULLS FIRST | NULLS LAST ]
  [, { expr | position | c_alias }
     [ ASC | DESC ]
     [ NULLS FIRST | NULLS LAST ]
  ]...'''
order_by_clause = (
    kw('order') + Optional(kw('siblings') + kw('by')) +
    sepmul((expression | nums | name) + Optional(kw('asc') | kw('desc'))
           + Optional(kw('nulls first') | kw('nulls last')), ','))

'''model_rules_clause =
[ RULES
  [ { UPDATE | UPSERT [ ALL ] } ]
  [ { AUTOMATIC | SEQUENTIAL } ORDER ]
  [ model_iterate_clause ]
]
( [ { UPDATE | UPSERT [ ALL ] } ]
cell_assignment [ order_by_clause ] = expr
  [,  [ { UPDATE | UPSERT [ ALL ] } ]
    cell_assignment [ order_by_clause ] = expr
  ]...
)'''
upd_ups_all = (kw('update') | kw('upsert') + Optional(kw('all')))
model_rules_clause = (
    Optional(kw('rules')
             + Optional(upd_ups_all)
             + Optional((kw('automatic') | kw('sequential')) + kw('order'))
             + Optional(model_iterate_clause))
    + '(' + sepmul(
        Optional(upd_ups_all) + cell_assignment + Optional(order_by_clause)
        + '=' + expression, ',')
    + ')')

'''main_model =
[ MAIN main_model_name ]
model_column_clauses
[ cell_reference_options ]
model_rules_clause'''
main_model = (Optional(kw('main') + name) + model_column_clauses + Optional(cell_reference_options) + model_rules_clause)

'''model_clause =
MODEL
   [ cell_reference_options ]
   [ return_rows_clause ]
   [ reference_model ]...
main_model'''
model_clause = kw('model') + Optional(cell_reference_options) + Optional(return_rows_clause) + ZeroOrMore(referenc_model) + main_model

'''reference_model =
REFERENCE reference_spreadsheet_name
ON (subquery)
model_column_clauses
  [ cell_reference_options ]'''
reference_model = (
    kw('reference') + name + kw('on') + '(' + subquery + ')'
    + model_column_clauses + Optional(cell_reference_options))

'''query_block =
SELECT
 [ hint ]
 [ { { DISTINCT | UNIQUE } | ALL } ]
select_list
  FROM { table_reference | join_clause | ( join_clause ) }
         [ , { table_reference | join_clause | (join_clause) } ] ...
  [ where_clause ]
  [ hierarchical_query_clause ]
  [ group_by_clause ]
  [ model_clause ]'''
from_item = (table_reference | join_clause | ('(' + join_clause + ')'))
query_block = (kw('SELECT') + Optional(hint)
    + Optional((kw('DISTINCT') | kw('UNIQUE')) | kw('ALL')) + select_list
    + kw('FROM') + sepmul(from_item, ',')
    + Optional(where_clause)
    + Optional(hierarchical_query_clause)
    + Optional(group_by_clause)
    + Optional(model_clause))

'''subquery =
{ query_block
| subquery { UNION [ALL] | INTERSECT | MINUS } subquery
    [ { UNION [ALL] | INTERSECT | MINUS } subquery ]...
| ( subquery )
} [ order_by_clause ]'''
subquery << (query_block
    | (subquery + OneOrMore(((kw('union') + Optional(kw('all'))) | kw('intersect') | kw('minus')) + subquery))
    | ('(' + subquery + ')')
    ) + Optional(order_by_clause)

'''for_update_clause =
FOR UPDATE
  [ OF [ [ schema. ] { table | view } . ] column
         [, [ [ schema. ] { table | view } . ] column
         ]...
  ]
  [ { NOWAIT | WAIT integer
    |  SKIP LOCKED
    }
  ]'''
for_update_clause = (
    kw('for update') + Optional(kw('of') + Optional(sepmul(Optional(name + '.') + name + '.'), ',')))
    + Optional((kw('nowait') | (kw('wait') + nums)) | kw('skip locked')))

'''dml_table_expression_clause =
{ [ schema. ]
  { table
    [ partition_extension_clause
    | @ dblink
    ]
  | { view | materialized view } [ @ dblink ]
  }
| ( subquery [ subquery_restriction_clause ] )
| table_collection_expression
}'''
dml_table_expression_clause = (
    (Optional(name + '.') + (name + Optional(partition_extension_clause | dblink) | (name + Optional(dblink))))
    | ('(' + subquery + Optional(subquery_restriction_clause) + ')')
    | table_collection_expression
)

'''insert_into_clause =
INTO dml_expression_clause [ t_alias ];'''
insert_into_clause = KW('INTO') + dml_expression_clause + Optional(t_alias)

'''bounds_clause =
{ lower_bound .. upper_bound
| INDICES OF collection [ BETWEEN lower_bound AND upper_bound ]
| VALUES OF index_collection
};'''
bounds_clause = ((lower_bound + '..' + upper_bound)
    | (kw('INDICES OF') + collection + Optional(KW('BETWEEN') + lower_bound + KW('AND') + upper_bound)
    | (kw('VALUES OF') + index_collection)))

'''forall_statement =
FORALL index IN bounds_clause [ SAVE EXCEPTIONS ] dml_statement EOS;'''
forall_statement = (KW('FORALL') + index + KW('IN') + bounds_clause
    + Optional(kw('SAVE EXCEPTIONS')) + dml_statement + EOS)

'''for_loop_statement =
[ FOR index IN [ REVERSE ] lower_bound .. upper_bound
    LOOP statement... END LOOP [ label ]  EOS;'''
for_loop_statement = (KW('FOR') + index + KW('IN') + Optional(KW('REVERSE'))
    + lower_bound + '..' + upper_bound
    + KW('LOOP') + OneOrMore(statement) + kw('END LOOP') + Optional(label)
    + EOS)

'''cursor_for_loop_statement =
[ FOR record IN
  { cursor [ ( cursor_parameter_declaration
               [ [,] cursor_parameter_declaration ]... )]
  | ( select_statement )
  }
    LOOP statement... END LOOP [label]  EOS;'''

'''inline_pragma =
PRAGMA INLINE ( subprogram , { 'YES' | 'NO' } )  EOS;'''
inline_pragma = (kw('pragma inline') + '(' + subprogram + ','
                 + (kw('yes') | kw('no')) + ')' + EOS)

'''exception_handler =
WHEN { exception [ OR exception ]... | OTHERS }
  THEN statement [ statement ]...;'''
exception_handler = (kw('when')
  + (kw('others')
    | (exception + ZeroOrMore(kw('or') + exception))
  + kw('then') + OneOrMore(statement)))

'''procedure_heading =
PROCEDURE procedure [ ( parameter_declaration [, parameter_declaration ]... ) ];'''
procedure_heading = (kw('procedure') + name
    + Optional('(' + sepmul(parameter_declaration, ',') + ')'))

'''procedure_definition =
procedure_heading { IS | AS }
  { [ declare_section ] body | call_spec | EXTERNAL };'''
procedure_definiton = procedure_heading + isas + (
  (Optional(declare_section) + body) | call_spec | kw('external'))

'''procedure_declaration =
procedure_heading;'''
procedure_declaration = procedure_heading

'''sql_statement =
{ commit_statement
| delete_statement
| insert_statement
| lock_table_statement
| rollback_statement
| savepoint_statement
| set_transaction_statement
| update_statement
};'''
sql_statement = (
  commit_statement
| delete_statement
| insert_statement
| lock_table_statement
| rollback_statement
| savepoint_statement
| set_transaction_statement
| update_statement)

'''procedure_call =
procedure [ ( [ parameter [, parameter ]... ] ) ]  EOS;'''
procedure_call = (name + Optional('('
    + Optional(sepmul(parameter, ',')) + ')') + EOS)

'''table_reference =
[ schema.] db_table_view
  { PARTITION ( partition ) | SUBPARTITION ( subpartition ) | @dblink }'''
table_reference = Optional(schema + '.') + db_table_or_view + (
    ((kw('subpartition') | kw('partition')) + '(' + name + ')') | ('@' + name))

'''select_into_statement =
SELECT [ { DISTINCT | UNIQUE } | ALL ]
  { * | select_item [[,] select_item ]... }
    { into_clause | bulk_collect_into_clause }
        FROM { table_reference | [ THE ] ( subquery ) } [ alias ]
          [ { table_reference | [ THE ] ( subquery ) } [ alias ] ]...
            rest-of-statement ;
'''
from_item = (table_reference | (kw('THE') + '(' + subquery + ')')) + Optional(alias)
select_into_statement = (kw('SELECT')
    + Optional((kw('DISTINCT') | kw('UNIQUE')) | kw('ALL'))
    + (Literal('*') | sepmul(select_item, ','))
    + (into_clause | bulk_collect_into_clause)
    + kw('FROM') + sepmul(from_item, ',')
    + rest_of_statement)

'''statement =
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
{ item_list_1 [ item_list_2 ] | item_list_2 };'''

isas = KW('IS') | KW('AS')

'''function_heading =
FUNCTION function [ ( parameter_declaration [, parameter_declaration ] ) ]
  RETURN datatype;'''
function_heading = KW('FUNCTION') + name + Optional('(' + sepmul(parameter_declaration, ',') + ')') + KW('RETURN') + datatype

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
  | (KW('RESULT_CACHE') + Optional(relies_on_clause))) + isas + ((Optional(declare_section) + body)
            | call_spec | KW('EXTERNAL'))

'''function_declaration =
function_heading
  [ DETERMINISTIC | PIPELINED | PARALLEL_ENABLE | RESULT_CACHE ]...  EOS;'''
function_declaration = (function_heading + ZeroOrMore(*map(KW,
    'DETERMINISTIC PIPELINED PARALLEL_ENABLE RESULT_CACHE'.split()))
    + EOS)

'''plsql_block =
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
statement << ZeroOrMore("<<" + name + ">>") + (
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
create_package = (KW('CREATE') + Optional(kw('OR REPLACE'))
    + KW('PACKAGE') + Optional(name + '.') + name + invoker_rights_clause + isas
    + declare_section + KW('END') + EOS)

'''
create_package_body =
CREATE [ OR REPLACE ] PACKAGE BODY [ schema. ] package_name
{ IS | AS } declare_section [ initialize_section ]
END [ package_name ]  EOS;
'''
create_package_body = (kw('create') + Optional(kw('or replace'))
    + kw('package body') + Optional(schema + '.') + name + isas
    + declare_section + Optional(initialize_section)
    + kw('end') + name + EOS)
