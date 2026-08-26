# utc.to.week()

## Syntax:
`function long utc.to.week( domain ttutc utc, ref long week_dayno, ref long year_dayno, ref long weekno, ref long hours, ref long minutes, ref long seconds, [ ref long yearno ] )`

## Description
This converts a UTC long format value to the corresponding day of the week, day of the year, week of the year, and so on, in local time.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `utc` |  The UTC long format value.  |
| `ref long` | `week_dayno` |  The day of the week. This depends on which day is defined as the first day of the week in the user data settings in the data dictionary.  |
| `ref long` | `year_dayno` |  The day number in the year.  |
| `ref long` | `weekno` |  The week number in the year. See Week handling.  |
| `ref long` | `hours` |  The time of day.  |
| `ref long` | `minutes` |  |
| `ref long` | `seconds` |  |
| `[ ref long` | `yearno ]` |  The year number. This argument is optional.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 |  Error. For example: Any intermediate result involves a date before the year 1 or past the year 9999.  |
-

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  If the day of the week lies in the week that includes the turn of the year, *weekno* returns either 53, 0, or 1. The rules applied are:
- *Yearno* argument included
- If less that 4 days of the week belong to the old year, *weekno* returns 1 and *yearno* returns the number of the new year.
- If 4 or more days belong to the old year, *weekno* returns 53 and *yearno* returns the number of the old year.
- *Yearno* argument not included
- If the day belongs to the old year, weekno returns 53.
- If the day belongs to the new year and there are less that 4 days of the new year in the week, *weekno* returns 0.
- If the day belongs to the new year and there are more that 3 days of the new year in the week, *weekno* returns 1.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
