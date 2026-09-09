# db.check.row.domains()

## Syntax:
`function long db.check.row.domains( long table_id, ref string fld_name )`

## Description
This checks whether the current record of a specified table conforms to the domain definitions in the data dictionary. All fields of the record are checked in turn until an error occurs. The function returns when the first error is encountered.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `ref string` | `fld_name` |  This returns the name of the first incorrect field.  |

## Return values
| | |
|---|---|
| 0 | No errors. |
| -1 | Invalid table ID. |
| ENOTINRANGE | Error in a field. |
If an error is returned, you can retrieve information about the specific error using [db.error.message()](db.error.message.md).

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
