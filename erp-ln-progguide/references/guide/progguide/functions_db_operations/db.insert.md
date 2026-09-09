# db.insert()

## Syntax:
`function long db.insert( long table_id, [ long mode, long eflag ] )`

## Description
This adds a new record to a specified table. The record pointer does not change.

## Arguments
| | |
|---|---|
| DB.RETRY | Set this value if retry points are being used. The actual database action is postponed until the transaction is committed. |
| 0 | When no retry point is used. This is default value. |

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
