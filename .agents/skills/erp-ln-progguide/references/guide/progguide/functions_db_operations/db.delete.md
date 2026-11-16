# db.delete()

## Syntax:
`function long db.delete( long table_id, [ long mode, long eflag ] )`

## Description
This deletes the current record. The record pointer is not changed, so the current record is undefined after the record has been deleted.

## Arguments
| | |
|---|---|
| DB.RETRY | Set this value if retry points and the SELECT FOR UPDATE statement are being used. The actual database action is postponed until the transaction is committed. |
| DB.DELAYED.LOCK | This option is available only for records for which a delayed lock has been set with [db.eq()](db.eq.md). |
| 0 | When the record is locked with DB.LOCK mode with one of the db functions like [db.eq()](db.eq.md), [db.next()](db.next.md) etc. This is default value. |

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
