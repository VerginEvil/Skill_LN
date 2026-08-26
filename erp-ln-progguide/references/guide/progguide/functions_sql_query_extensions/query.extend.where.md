# query.extend.where()

## Syntax:
`function void query.extend.where( string extension_string, [ long mode ] )`

## Description
Use this to construct a query extension for the WHERE clause of a database query. Use this function for non-zoom sessions. Use [query.extend.where.in.zoom()](query.extend.where.in.zoom.md) for defining query filters for zoom sessions.

## Arguments
| | | |
|---|---|---|
| `string` | `extension_string` |  A string containing conditions to be included in the WHERE statement. The main-table and table/aliases named in query.extend.from() can be used.  |
| `[ long` | `mode ]` |  This optional argument can have one of the following values:  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  In Infor Enterprise Server, this function replaces the predefined variable *query.extension* that was used in earlier versions of the software.
The combination of query.define.sort.order and use of combined field statement in the query.extend.where will give unpredictable results
Overwrite after the before.program with the use of other tables gives unpredictable results. This can be the result of active extensions. Use of unique aliases will avoid this.
This function can be used in extensions; it must not overule the query of the Standard LN session.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Query extensions sample program](example.md)
