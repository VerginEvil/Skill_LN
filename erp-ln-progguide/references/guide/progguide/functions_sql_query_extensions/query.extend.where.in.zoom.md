# query.extend.where.in.zoom()

## Syntax:
`function void query.extend.where.in.zoom( string extension_string )`

## Description
Use this to construct a query extension for the WHERE clause of a database query. Use this function for zoom sessions. Use [query.extend.where()](query.extend.where.md) for defining query filters in non-zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing conditions to be included in the WHERE statement.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  In Infor Enterprise Server, this function replaces the predefined variable *query.extension* that was used in earlier versions of the software.
This function can be used in extensions; it must not overule the query of the Standard LN session.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
