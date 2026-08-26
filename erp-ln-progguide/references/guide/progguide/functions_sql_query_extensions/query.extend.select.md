# query.extend.select()

## Syntax:
`function void query.extend.select( string extension_string, [ long mode ] )`

## Description
Use this to construct a query extension for the SELECT clause of a database query. Use this function for non-zoom sessions. Use [query.extend.select.in.zoom()](query.extend.select.in.zoom.md) for defining query filters for zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the names of the fields or a sub-query to be included in the SELECT statement. Use commas [,] to separate the field names. The prefix of the column is a table or alias of the query.extend.from().  |
| `[ long` | `mode ]` |  This optional argument can have one of the following values:  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
