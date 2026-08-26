# query.extend.select.in.zoom()

## Syntax:
`function void query.extend.select.in.zoom( string extension_string )`

## Description
Use this to construct a query extension for the SELECT clause of a database query. Use this function for zoom sessions. Use [query.extend.select()](query.extend.select.md) for defining query filters in non-zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the names of the fields to be included in the SELECT statement. Use commas [,] to separate the field names.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
