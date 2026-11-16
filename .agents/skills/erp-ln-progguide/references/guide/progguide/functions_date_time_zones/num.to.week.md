# num.to.week()

## Syntax:
`function long num.to.week( long dayno, ref long week_dayno, ref long year_dayno, ref long weekno, [ ref long yearno ] )`

## Description
This converts a specified number of days since 01-01-0001 to the corresponding day of the week, day of the year, and week number of the year.

## Arguments
| | | |
|---|---|---|
| `long` | `dayno` |  A number of days since 01-01-0001. This value must be at least 1 (corresponding to January 1 of the year 1) and less than 3,652,060 (corresponding to January 1 of the year 10,000). Other values lead to an error.  |
| `ref long` | `week_dayno` |  The day of the week. This depends on which day is defined as the first day of the week in the user data settings in the data dictionary.  |
| `ref long` | `year_dayno` |  The day number in the year.  |
| `ref long` | `weekno` |  The week number in the year. See [Week handling](overview.md#week_handling).  |
| `[ ref long` | `yearno ]` |  The year number. This argument is optional.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  If the day of the week lies in the week that includes the turn of the year, *weekno* returns either 53, 0, or 1. The rules applied are:

- If less that 4 days of the week belong to the old year, *weekno* returns 1 and *yearno* returns the number of the new year.

- If 4 or more days belong to the old year, *weekno* returns 53 and *yearno* returns the number of the old year.

- If the day belongs to the old year, weekno returns 53.

- If the day belongs to the new year and there are less that 4 days of the new year in the week, *weekno* returns 0.

- If the day belongs to the new year and there are more that 3 days of the new year in the week, *weekno* returns 1.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
