# query.extend.from.in.zoom()

## Syntax:
`function void query.extend.from.in.zoom( string extension_string )`

## Description
Use this to construct a query extension for the FROM clause of a database query. Use this function for zoom sessions. Use [query.extend.from()](query.extend.from.md) for defining query filters in non-zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the names of the tables to be included in the FROM statement. Use commas [,] to separate the tables names. This function can be used in extensions; it must not overule the query of the Standard LN session.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)

- [SQL query extensions synopsis](synopsis.md)

- [Query extensions sample program](example.md)
