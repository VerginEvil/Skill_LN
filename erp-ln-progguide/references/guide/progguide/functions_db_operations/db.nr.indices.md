# db.nr.indices()

## Syntax:
`function long db.nr.indices( long table_id, ref long nr_indices )`

## Description
This returns the number of indices that exist on a specified table.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `ref long` | `nr_indices` |  Returns the number of indices on the table.  |

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
