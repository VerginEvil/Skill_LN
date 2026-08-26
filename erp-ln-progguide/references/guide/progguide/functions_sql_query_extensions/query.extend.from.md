# query.extend.from()

## Syntax:
`function void query.extend.from( string extension_string, [ long mode ] )`

## Description
Use this to construct a query extension for the FROM clause of a database query. Use this function for non-zoom sessions. Use [query.extend.from.in.zoom()](query.extend.from.in.zoom.md) for defining query filters for zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the names of the tables to be included in the FROM statement. Use commas [,] to separate the table names. Format of extension_string is: table1 [alias1] [, table2 [alias2][, table3 [alias3] ... When a table is named as alias, the alias must be referenced in query.extend.select() and query.extend.where(). This function can be used in extensions; it must not overule the query of the Standard LN session.  |
| `[ long` | `mode ]` |  This optional argument can have one of the following values:  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
