# num.to.date()

## Syntax:
`function long num.to.date( long dayno, ref long yearno, ref long monthno, ref long month_dayno )`

## Description
This converts a specified number of days since 01-01-0001 to the corresponding year, month, and day of the month.

## Arguments
| | | |
|---|---|---|
| `long` | `dayno` |  A number of days since 01-01-0001. This value must be at least 1 (corresponding to January 1 of the year 1) and less than 3,652,060 (corresponding to January 1 of the year 10,000). Other values lead to an error.  |
| `ref long` | `yearno` |    |
| `ref long` | `monthno` |    |
| `ref long` | `month_dayno` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
