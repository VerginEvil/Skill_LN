# sql.select.bind()

## Syntax:
`function long sql.select.bind( long sql_id, long pseudo_var, varname var_name(.) )`

## Description
When you define an SQL statement with the [sql.parse()](sql.parse.md) function, you can define a pseudo variable for any or all of the fields specified in the SELECT statement. You do this by appending a number, prefixed by a colon [:], to each field. You use *sql.select.bind()* to bind a pseudo variable to a BAAN 4GL variable. As a result, the values of the field retrieved by the SELECT statement are stored in the 4GL variable. They can then be used elsewhere in the program.
Note that it is not necessary to bind external variables.

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |  The query ID, as returned by [sql.parse()](sql.parse.md).  |
| `long` | `pseudo_var` |  The pseudo variable from the SELECT list. This is always a number.  |
| `varname` | `var_name(.)` |  The name of the BAAN 4GL variable to which the pseudo variable must be bound.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long sql_id
domain tccom.bpid, customer

sql_id = sql.parse( "select tccom100.cuno:1 " &  "from
tccom100" )
sql.select.bind( sql_id, 1, customer )
.....
print customer
```

## Related topics
- [Dynamic SQL queries overview](overview.md)
- [Dynamic SQL queries synopsis](synopsis.md)
