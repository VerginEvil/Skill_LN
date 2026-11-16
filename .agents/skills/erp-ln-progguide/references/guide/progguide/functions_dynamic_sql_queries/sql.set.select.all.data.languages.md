# sql.set.select.all.data.languages()

## Syntax:
`function boolean sql.set.select.all.data.languages( boolean select.all.data.languages )`

## Description
This function sets the value of the `select.all.data.languages` flag of the current process. The specified value of the flag remains in effect until the end of the current 3GL function. After return from the current 3GL function, the flag is set back to the value that it had in the calling 3GL function. When the program jumps back to a [retry point](../functions_database_handling/retry_points.md), the flag is set back to the value that it had at the moment that the retry point was set.
When the value of the flag is true, it has the same influence as the annotation `cSqlAnnotation_SelectAllDataLanguages`.
For the (more or less deprecated) low level [database operations](../functions_db_operations/overview.md) for which the annotation `cSqlAnnotation_SelectAllDataLanguages` is not available, the `select.all.data.languages` flag does have its influence!

## Arguments
| | | |
|---|---|---|
| `boolean` | `select.all.data.languages` |  The new value of the `select.all.data.languages` flag of the current process.  |

## Return values
The old value of the `select.all.data.languages` flag of the current process.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2200.

## Related topics
- [Dynamic SQL queries overview](overview.md)

- [Dynamic SQL queries synopsis](synopsis.md)

- [sql.get.select.all.data.languages()](sql.get.select.all.data.languages.md)
