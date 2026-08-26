# db.check.restricted()

## Syntax:
`function long db.check.restricted( long table_id, long mode, ref string message(256) )`

## Description
In a table definition, it is possible to set restrictions on update and/or delete actions for records that are referenced by other tables. These restrictions mean that you cannot delete and/or update the primary key that is referenced by another table. This function checks whether there are references to the current record with delete and/or update restrictions. This function can take a long time to complete if no reference counter is kept (lookup mode).

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `long` | `mode` |  Use to specify whether you want to check for delete or update restrictions. Possible values are: 1 delete mode 2 update mode  |
| `ref string` | `message(256)` |  This returns the reference message of the table. This message is defined in the data dictionary.  |

## Return values
| | |
|---|---|
| 0 | No reference found. |
| 1 | One or more references found. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
