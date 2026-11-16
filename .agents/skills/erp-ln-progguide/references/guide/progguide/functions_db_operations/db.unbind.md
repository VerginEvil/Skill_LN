# db.unbind()

## Syntax:
`function long db.unbind( long table_id )`

## Description
This deletes the specified table pointer.

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
