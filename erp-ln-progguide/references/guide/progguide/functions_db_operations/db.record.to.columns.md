# db.record.to.columns()

## Syntax:
`function long db.record.to.columns( long table_id )`

## Description
When you bind to a table (see [db.bind()](db.bind.md) and specify that the default record buffer is to be used, the contents of the buffer are automatically copied to the table fields in your program script. This does not happen when you specify a record buffer other than the default buffer.
Therefore, when a record buffer is used which is not the default record buffer, the table fields will be invalid after the record buffer has changed and this function must be called to copy the field values from the record buffer to the table fields.

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
