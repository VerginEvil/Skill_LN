# sql.get.select.all.data.languages()

## Syntax:
`function boolean sql.get.select.all.data.languages( )`

## Description
This function retrieves the value of the `select.all.data.languages` flag of the current process.
When the value of the flag is true, it has the same influence as the annotation `cSqlAnnotation_SelectAllDataLanguages`.
For the (more or less deprecated) low level [database operations](../functions_db_operations/overview.md) for which the annotation `cSqlAnnotation_SelectAllDataLanguages` is not available, the `select.all.data.languages` flag does have its influence!

## Return values
The current value of the `select.all.data.languages` flag of the current process.

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2200.

## Related topics
- [Dynamic SQL queries overview](overview.md)
- [Dynamic SQL queries synopsis](synopsis.md)
- Inverse operation: [sql.set.select.all.data.languages()](sql.set.select.all.data.languages.md)
