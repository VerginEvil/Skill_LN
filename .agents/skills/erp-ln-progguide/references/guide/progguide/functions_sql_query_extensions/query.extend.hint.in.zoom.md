# query.extend.hint.in.zoom()

## Syntax:
`function void query.extend.hint.in.zoom( string extension_string )`

## Description
Use this to construct a query extension for the HINT clause of a database query. Use this function for zoom sessions. Use [query.extend.hint()](query.extend.hint.md) for defining query filters in non-zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the hint to be included in the HINT statement.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)

- [SQL query extensions synopsis](synopsis.md)

- [Query extensions sample program](example.md)
