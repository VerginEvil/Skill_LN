# query.extend.hint()

## Syntax:
`function void query.extend.hint( string extension_string, [ long mode ] )`

## Description
Use this to construct a query extension for the HINT clause of a database query. Use this function for non-zoom sessions. Use [query.extend.hint.in.zoom()](query.extend.hint.in.zoom.md) for defining query filters for zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing the hints to be included in the HINT statement.  |
| `[ long` | `mode ]` |  This optional argument can have one of the following values:  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
