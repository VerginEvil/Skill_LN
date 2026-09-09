# sql.where.bind()

## Syntax:
`function long sql.where.bind( long sql_id, long pseudo_var, varname var_name(.) )`

## Description
This binds a pseudo variable from the WHERE clause of a specified SQL query to a BAAN 4GL variable. This enables the BAAN 4GL variable to be used in the WHERE clause. Note that there is no need to bind external variables. The BAAN 4GL variable is evaluated when bound.

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |  The query ID, as returned by [sql.parse()](sql.parse.md).  |
| `long` | `pseudo_var` |  The pseudo variable from the WHERE clause. This is always a number. In the WHERE clause, it is entered as the number, prefixed by a colon [:].  |
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

string city(30)
long sql_id

city = "London"
sql_id = sql.parse( "select tccom000.* " & "from tccom000 "
&
        "where tccom000.city = :1" )
sql.where.bind(sql_id, 1, city)
```

## Related topics
- [Dynamic SQL queries overview](overview.md)

- [Dynamic SQL queries synopsis](synopsis.md)
