# query.extend.from()

## Syntax:
`function void query.extend.from( string extension_string, [ long mode ] )`

## Description
Use this to construct a query extension for the FROM clause of a database query. Use this function for non-zoom sessions. Use [query.extend.from.in.zoom()](query.extend.from.in.zoom.md) for defining query filters for zoom sessions.

## Arguments
| | |
|---|---|
| EXTEND_OVERWRITE | replaces any existing query extension (this is the default mode) |
| EXTEND_APPEND | appends this extension to the existing extension |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [SQL query extensions overview](overview.md)

- [SQL query extensions synopsis](synopsis.md)

- [Query extensions sample program](example.md)
