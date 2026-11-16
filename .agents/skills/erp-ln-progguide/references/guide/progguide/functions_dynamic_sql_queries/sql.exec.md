# sql.exec()

## Syntax:
`function long sql.exec( long sql_id )`

## Description
This initializes the specified query and evaluates any bind variables in the WHERE clause. Before calling this function, you must previously have called [sql.parse()](sql.parse.md) to define the query. The *sql_id* argument indicates the query ID, as returned by [sql.parse()](sql.parse.md).

## Arguments
| | | |
|---|---|---|
| `long` | `sql_id` |  the query ID, as returned by [sql.parse()](sql.parse.md)  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |
Note that executing an UPDATE or DELETE statement may result in error ENOREC, which means that the statement completed but no rows were processed.

## Context
This function is implemented in the porting set and can be used in all script types.

## Multi Language Data
By default, for multi language columns, execution of the query retrieves all data languages from the database.
If the [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0, then the default behavior is to retrieve only the current data language.
When the annotation `cSqlAnnotation_SelectAllDataLanguages` is used in the call of [sql.parse()](sql.parse.md), then it is enforced that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*.
Also, the [select.all.data.languages](sql.set.select.all.data.languages.md) flag can be used to enforce that the value of multi language fields is retrieved in all data languages. If the value of the `select.all.data.languages` flag differs from its value during the previous call of [sql.exec()](sql.exec.md) for the same query ID (or, if this is the first such call, during the call of [sql.parse()](sql.parse.md) which originally returned the query ID), then implicitly the query is parsed again. This is only done when it may be expected that the changed value of the `select.all.data.languages` flag will influence the result, i.e. when at least [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0 and the annotation `cSqlAnnotation_SelectAllDataLanguages` was not used in the call of [sql.parse()](sql.parse.md).
For tables which are configured for selection of all languages of its multi language fields (see the *mle_all_data_languages* argument for function [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)), execution of the query always retrieves all data languages.

## Related topics
- [Dynamic SQL queries overview](overview.md)

- [Dynamic SQL queries synopsis](synopsis.md)
