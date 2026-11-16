# inputstr.to.date()

## Syntax:
`function long inputstr.to.date( string inputstr(.), string format(7) )`

## Description
This converts a date input string to the number of days since 01-01-0001.

## Arguments
| | | |
|---|---|---|
| `string` | `inputstr(.)` |  The date input string, possibly input by the user and retrieved using the function [data.input()](../functions_char_b_win/data.input.md).  |
| `string` | `format(7)` |  Indicates the format of the input string, specified by using the substitution symbols %D *xxx* [, *lang*].  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Return value
| | |
|---|---|
|  | The number of days from 01-01-0001 to the date specified in the input string. |
| -1 | Error. |

## Example
This example assumes that %D002,3 represents the format MDY.
```

long dat
dat = inputstr.to.date( "06171991", "%D002,3" )
| dat now contains 727000
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
