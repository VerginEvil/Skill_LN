# db.ge()

## Syntax:
`function long db.ge( long table_id, [ long lock ] )`

## Description
This reads from a specified table the record whose key value is greater than or equal to a certain predefined value. Before calling *db.ge()*, you must assign the required value to the key field. For example:
```

tiitm001.item = "001"
db.ge( ttiitm001 )
```

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `[ long` | `lock ]` |  By default, the record is not locked before reading. Use this optional argument to apply a lock to the record. The possible values are: DB.LOCK lock record for update DB.DELAYED.LOCK apply a delayed lock to the record; the lock is applied immediately before the update action  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Multi Language Data
By default, for multi language columns, this function retrieves all data languages from the database.
If the [resource](../misc/bshell_resources.md) *mle_all_data_languages* has the value 0, then the default behavior is to retrieve only the current data language.
The [select.all.data.languages](../functions_dynamic_sql_queries/sql.set.select.all.data.languages.md) flag can be used to enforce that the value of multi language fields is retrieved in all data languages, independent of the setting of [resource](../misc/bshell_resources.md) *mle_all_data_languages*.
For this function, there is no way to apply the annotation `cSqlAnnotation_SelectAllDataLanguages` to override the default behavior. Remember: this function is supported for backward compatibility only. In new applications, use queries instead.
However, for tables which are configured for selection of all languages of its multi language fields (see the *mle_all_data_languages* argument for function [rdi.table()](../functions_runtime_dictionary_information/rdi.table.md)), this function always retrieves all data languages.
Furthermore, when this function applies a lock to the selected record, also all data languages are retrieved for the multi language columns of the locked record.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
