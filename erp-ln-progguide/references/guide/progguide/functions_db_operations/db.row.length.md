# db.row.length()

## Syntax:
`function long db.row.length( long table_id, ref long row_length )`

## Description
Use this to retrieve the length of records in a specified table.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `ref long` | `row_length` |  This returns the length of the internal buffer that is needed for a row in the table and its internal data like '_compnr' and '_dlock'. (see also the int_length of rdi.table())  |

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
