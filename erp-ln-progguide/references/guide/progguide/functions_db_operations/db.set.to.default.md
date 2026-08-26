# db.set.to.default()

## Syntax:
`function long db.set.to.default( long table_id )`

## Description
This sets bound variables in the program script to the default values defined in the data dictionary.

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
