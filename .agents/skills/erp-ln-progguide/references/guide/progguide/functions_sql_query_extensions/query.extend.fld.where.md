# query.extend.fld.where()

## Syntax:
`function long query.extend.fld.where( string select_column, string where_condition )`

## Description
With the query.extend.fld… interface the metadata is stored in the 4gl engine. The query.extend.fld… information is used to build the standard query for retrieving requested data, inclusive the application fields. The result is used for the display of the field. The value of easy filter on the application field and the query.extend.fld… information is used to extend the WHERE clause of the standard query. The standard query is used to display the session.
SQL expression for the WHERE clause of the select column. This expression will be added to the standard query for selecting the rows.
The query query.extend.fld... functionality is based on the main table of the session. All the used references must be defined. Existing relations in the session can be used as template, but must be added. The reason to declare all used references is the existing of them. With personalize form and possibility to change (overwrite) the present reference the reference can be removed from the standard query. Defining a reference more then once is taken in account.
( see example [query.extend.fld.select()](query.extend.fld.select.md) or [query.extend.fld.from()](query.extend.fld.from.md))
You can use this function in the section before.program.

## Arguments
| | | |
|---|---|---|
| `string` | `select_column` |  Name of the form field in the form.  |
| `string` | `where_condition` |  SQL instruction for WHERE clause.  |

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
