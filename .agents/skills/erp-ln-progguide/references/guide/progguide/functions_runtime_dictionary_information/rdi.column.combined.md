# rdi.column.combined()

## Syntax:
`function long rdi.column.combined( string column_name(18), string ref child_colums(18, 32) )`

## Description
This returns information about the child columns of a specified column.

## Arguments
| | | |
|---|---|---|
| `string` | `column_name(18)` |  The name of the column for which you wish to retrieve information.  |
| `string` | `ref child_colums(18, 32)` |  This returns an array containing the names of the child columns of the specified column. It can contain the names of up to 32 child columns.  |

## Return values
The function returns the number of filled children.
-1 indicates that the column does not exist, or is not combined

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
