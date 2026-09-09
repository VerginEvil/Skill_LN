# week.to.num()

## Syntax:
`function long week.to.num( long weekno, long yearno, long week_dayno )`

## Description
This returns the number of days since 01-01-0001 for a specified week number, year number, and day of the week. The day of the week is interpreted by using the day defined as the first day of the week in the user data settings in the data dictionary (see [Week handling](overview.md#week_handling)).

## Arguments
| | | |
|---|---|---|
| `long` | `weekno` |    |
| `long` | `yearno` |    |
| `long` | `week_dayno` |    |

## Return values
| | |
|---|---|
|  | The number of days since 01-01-0001. |
| -1 | Error. For example, the date is before the year 1 or past the year 9999. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
