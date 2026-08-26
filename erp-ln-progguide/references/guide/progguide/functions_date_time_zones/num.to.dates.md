# num.to.date$()

## Syntax:
`function string num.to.date$( long dayno, long mode )`

## Description
This converts a specified number of days since 01-01-0001 to the corresponding date, formatted as a date string. The sequence of day, month, and year in the string depends on the user data settings defined in the data dictionary (default is "YYMMDD"). The separator character used is also defined in the data dictionary (default is '/').

## Arguments
| | | |
|---|---|---|
| `long` | `dayno` |  A number of days since 01-01-0001. This value must be at least 1 (corresponding to January 1 of the year 1) and less than 3,652,060 (corresponding to January 1 of the year 10,000). Other values lead to an error.  |
| `long` | `mode` |  Specifies certain characteristics of the date string format: 0: Date like YYMMDD without separators (for example, "011231") 1: Date like YY/MM/DD with separators (for example,"01/12/31") 2: Date like YYYYMMDD without separators (for example, "20101231") 3: Date like YYYY/MM/DD with separators (for example,"2010/12/31").  |

## Return values
| | |
|---|---|
|  | The formatted date string. |
|  | Or an empty string if an error occurs. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
