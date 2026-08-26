# query.extend.fld.from()

## Syntax:
`function long query.extend.fld.from( string select_column, string extension_string )`

## Description
With the query.extend.fld… interface the metadata is stored in the 4gl engine. The query.extend.fld… information is used to build the standard query for retrieving requested data, inclusive the application fields. The result is used for the display of the field. The value of easy filter on the application field and the query.extend.fld… information is used to extend the WHERE clause of the standard query. The standard query is used to display the session.
Use this to construct a query extension for the FROM clause of a database query. This expression will be added to the standard query for retrieving the column as form field. ( see [query.extend.fld.select()](query.extend.fld.select.md) or [query.extend.fld.where()](query.extend.fld.where.md))
You can use this function in the section before.program.

## Arguments
| | | |
|---|---|---|
| `string` | `select_column` |  Name of the form field in the form.  |
| `string` | `extension_string` |  A string containing the names of the tables to be included in the FROM statement. Use commas [,] to separate the table names.  |

## Return values
| | |
|---|---|
| 0 | On success. |
| <> 0 | error |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## TIV
This function is available from Enterprise Server TIV level 2100 and is only usable in LN-UI.

## Related topics
- [SQL query extensions overview](overview.md)
- [SQL query extensions synopsis](synopsis.md)
- [Column filtering](column_filtering.md)
- [Query extensions sample program](example.md)
