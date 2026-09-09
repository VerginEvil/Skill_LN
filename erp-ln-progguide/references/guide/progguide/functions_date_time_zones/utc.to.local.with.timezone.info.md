# utc.to.local.with.timezone.info()

## Syntax:
`function long utc.to.local.with.timezone.info( domain ttutc utc, ref long local_days, ref long local_time, ref long utcdiff )`

## Description
This converts a [UTC](overview.md#utc) long format value to local date and time. The difference in seconds to UTC is returned in the variable utcdiff.

## Arguments
| | | |
|---|---|---|
| `domain ttutc` | `utc` |  The UTC long format value.  |
| `ref long` | `local_days` |  The local date as the number of days since 01-01-0001.  |
| `ref long` | `local_time` |  The local time as the number of seconds since 00:00 hour.  |
| `ref long` | `utcdiff` |  The number of seconds the current timezone of the user is away from UTC.  |

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
