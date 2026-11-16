# rdi.table.referenced()

## Syntax:
`function long rdi.table.referenced( string table_name(9), long referring_index, ref string referring_column_name(18), ref long ref_mode )`

## Description
This returns information about columns referring to this table.

## Arguments
| | | |
|---|---|---|
| `string` | `table_name(9)` |  The name of the table about which you want to retrieve information.  |
| `long` | `referring_index` |  The index of the referring column.  |
| `ref string` | `referring_column_name(18)` |  This returns the name of the column referring to this table.  |
| `ref long` | `ref_mode` |  This returns the relation type. Possible values are: 1 mandatory 2 mandatory unless empty 3 not mandatory  |

## Return values
0 success
-1 index too high
-2 error

## Context
This function is implemented in the porting set and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
