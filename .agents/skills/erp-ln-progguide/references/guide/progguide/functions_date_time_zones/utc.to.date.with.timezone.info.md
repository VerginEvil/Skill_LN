# utc.to.date.with.timezone.info()

## Syntax:
`function long utc.to.date.with.timezone.info( domain ttutc utc, ref long yearno, ref long monthno, ref long month_dayno, ref long hours, ref long minutes, ref long seconds, ref long utcdiff )`

## Description
This converts a [UTC](overview.md#utc) long format value to the corresponding year, month, day, and so on, in local time. The difference in seconds to UTC is returned in the variable utcdiff.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `utc` |    |
| `ref long` | `yearno` |    |
| `ref long` | `monthno` |    |
| `ref long` | `month_dayno` |    |
| `ref long` | `hours` |    |
| `ref long` | `minutes` |    |
| `ref long` | `seconds` |    |
| `ref long` | `utcdiff` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. For example: Any intermediate result involves a date before the year 1 or past the year 9999. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
