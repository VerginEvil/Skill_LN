# rdi.tablefield.sensitivity()

## Syntax:
`function long rdi.tablefield.sensitivity( const string tablefield )`

## Description
Returns sensitivity of the provided table field.

## Arguments
| | | |
|---|---|---|
| `const string` | `tablefield` |  the name of table field for which you need to know the sensitivity.  |

## Return values
A value of 0 means that the report is not sensitive. A value of 1 - 99 is the sensitivity level. A value of < 0 or > 99 indicates an error.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)

- [Tools Interface Version (TIV)](../tiv/tiv_overview.md)
