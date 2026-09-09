# sum.records.in.view()

## Syntax:
`function void sum.records.in.view( const string column1.var, double result1.var, [ const string, double...,... ] )`

## Description
This function performs a query on the maintable of the session, including all reference tables, and will sum the values of each specified column. The query will take the current view fields, active user filter and any query extensions into account. Preconditions - an even number of parameters must be passed - any specified column must exist in the datadictionary if one of these conditions is not met, an assert is given Parameters column the name of column to sum result the result of the sum operation for 'column'... more pairs of 'column' and 'result'

## Arguments

## field or expression to sum

## result of sum fieldname1
| | | |
|---|---|---|
| `const string` | `column1.var` |  specify the field/expression to sum. fieldname or fieldname in expression must exist in the maintable or in the referenced tables. column1.var must be a decimal field.  |
| `double` | `result1.var` |  specify the output field to receive the sum.  |
| `[ const string, double` | `...,... ]` |  next pair of [column.var, result.var]. Use these optional pair of arguments to sum other columns. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Notes  An even number of parameters must be passed.
When specified a field as column, the column must exist in the datadictionary.
For fields in expression is the expression evaluated by the SQL engine.
Asserts  No Columns in input.
No navigation present yet.
Column [string] doesn't exist.
Type column [string] is not DOUBLE, INTEGER, LONG or FLOAT.
Missing element for repeating field, syntax: 'fieldname(n)' with n equals occurrence element.
Syntax of query error.

## Example
```

on.display.total.line:
	double    sum_field
	double    sum_expression
	double    sum_repeatingField

	sum.records.in.view( "field", sum_field, "xxnum1*xxnum2", sum_expression, "xxrepeatLong(1)", sum_repeatingFieldOccur1 )
	display.total.fields( "xxtable.field", sum_field )
	display.total.fields( "xxtable.expr", sum_expression )
	display.total.fields( "xxrepeatLong", sum_repeatingFieldOccur2 )
```

## TIV
This function is available from TIV level 1753 till 1800, 1802 and higher.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
