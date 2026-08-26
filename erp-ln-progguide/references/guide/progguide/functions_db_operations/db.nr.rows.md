# db.nr.rows()

## Syntax:
`function long db.nr.rows( long table_id, ref long nr_rows, [ long comp_nr ] )`

## Description
This returns the number of rows that a specified table contains.

## Arguments
| | | |
|---|---|---|
| `long` | `table_id` |  The table ID, as returned by [db.bind()](db.bind.md).  |
| `ref long` | `nr_rows` |  Returns the number of rows in the table.  |
| `[ long` | `comp_nr ]` |  This optional argument specifies a company number for the table. The default company is the company of the user.  |

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
