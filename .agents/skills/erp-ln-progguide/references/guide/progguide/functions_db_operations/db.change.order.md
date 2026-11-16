# db.change.order()

## Syntax:
`function long db.change.order( long table_id, long index_nr, [ long compnr ] )`

## Description
This makes a specified index the current index. After this action, the record pointer is undefined.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `long` | `index_nr` |  The number of the index that you want to become the current index. The index must exist.  |
| `[ long` | `compnr ]` |  This optional argument specifies a company number for the table. The default company is the company of the user.  |

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
