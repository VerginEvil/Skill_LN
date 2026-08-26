# week.to.utc()

## Syntax:
`function domain ttutc week.to.utc( long weekno, long yearno, long week_dayno, long hours, long minutes, long seconds )`

## Description
This converts a specified week number, year number, day number in week, and so on, in local time, to UTC long format. For information on week numbering, see Week handling. Input values must be in the signed 32-bit value range.

## Arguments
| | | |
|---|---|---|
| `long` | `weekno` |  |
| `long` | `yearno` |  |
| `long` | `week_dayno` |  |
| `long` | `hours` |  |
| `long` | `minutes` |  |
| `long` | `seconds` |  |

## Return values
| | |
|---|---|
| >= 0 | The UTC long format value. |
| -1 |  Error. For example: Any intermediate result involves a date before the year 1 or past the year 9999. The exact result is negative or greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range.  |
-
-

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
