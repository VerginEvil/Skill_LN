# rdi.is.application.column()

## Syntax:
`function boolean rdi.is.application.column( const string column.name, [ long column.type, long column.offset, long table.real.length ] )`

## Description
This function checks whether the given column is an application column, or one that is automatically added by tools.
Note  Indices, combined fields, rcd_utc, and _compnr (among others) are *not* considered to be application columns by this function.
Either only the first, or all parameters must be specified. The optional parameters can be used to prevent this function from calling [rdi.table()](rdi.table.md) and [rdi.column()](rdi.column.md) again when that was already done by the application.
Note  Customer Defined Fields *are* considered application columns. These can be distinguished using the `DB.CDF` bit set in the `flag` parameter returned by [rdi.column()](rdi.column.md) or [rdi.table.column()](rdi.table.column.md)

## Arguments
| | | |
|---|---|---|
| `const string` | `column.name` |  The column (including table name) to check.  |
| `[ long` | `column.type ]` |  Optional input, the column's database type as returned by e.g. [rdi.column()](rdi.column.md).  |
| `[ long` | `column.offset ]` |  Optional input, the column's offset in the record as returned by e.g. [rdi.column()](rdi.column.md).  |
| `[ long` | `table.real.length ]` |  Optional input, the table record's length without internal data as returned by [rdi.table()](rdi.table.md) (real_length).  |

## Return values
True if the column is a regular application column, false if the column is one that is automatically added by tools.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2040.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
