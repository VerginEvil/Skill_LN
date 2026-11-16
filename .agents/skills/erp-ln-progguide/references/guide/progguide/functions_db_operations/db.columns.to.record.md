# db.columns.to.record()

## Syntax:
`function long db.columns.to.record( long table_id )`

## Description
The record buffer of a table is used for reading records from, or writing records to, that table. When you bind to a table (see [db.bind()](db.bind.md)) and specify that the default record buffer is to be used, the contents of the table fields are automatically copied to the buffer. This does not happen when you specify a record buffer other than the default buffer.
Therefore, when a record buffer is used which is not the default record buffer, the record buffer may not contain the same field values as the table fields. This function can be called to copy the field values from the table fields to the record buffer. The record buffer must contain the correct field values before reading from, or writing to, the database.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <> 0 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
