# date.to.inputstr$()

## Syntax:
`function string date.to.inputstr$( long dayno, string format(7), long length )`

## Description
This converts a specified number of days since 01-01-0001 to a date input string.

## Arguments
| | | |
|---|---|---|
| `long` | `dayno` |  A number of days since 01-01-0001.  |
| `string` | `format(7)` |  The format for the date string, specified by using the substitution symbols %Dxxx[,lang]  |
| `long` | `length` |  The length of the date string: 6: year represented by 2 characters (century not included) 8: year represented by 4 characters (century included)  |

## Return values
| | |
|---|---|
|  | The formatted input string. |
|  | An empty string if an error occurs. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example creates a default input string for the [data.input()](../functions_char_b_win/data.input.md) function.
```

string inpstring(8)
inpstring = date.to.inputstr$( 727000, "%D002,3", 8 )
```
If the %D002 format for language 3 is MDY, the string returned is "06171991" (that is, June 17, 1991). If it is DWY, and the first day of the week is Sunday, the string returned is "2251991" (that is, day 2, week 25, 1991).

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
