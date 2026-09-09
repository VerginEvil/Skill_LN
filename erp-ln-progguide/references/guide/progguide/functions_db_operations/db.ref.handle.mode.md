# db.ref.handle.mode()

## Syntax:
`function long db.ref.handle.mode( string table_name, long mode )`

## Description
Use this to check whether a full table scan (FTS) is necessary during delete or update operations. Delete and update operations can take a long time to complete when the table is referenced by other tables but no reference counter is kept (cascade, nullify, or lookup mode). When there is no index on the foreign key in the child table, normally a full table scan is required to search for referring records.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name` |  The table name, without the leading 't' character.  |
| `long` | `mode` |  Possible modes: DB.REF.UPDATE DB.REF.DELETE  |

## Return values
| | |
|---|---|
| 0 | Full table scan is not necessary. |
| 1 | Full table scan is necessary. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
