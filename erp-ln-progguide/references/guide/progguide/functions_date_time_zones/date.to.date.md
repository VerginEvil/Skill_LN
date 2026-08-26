# date.to.date()

## Syntax:
`function long date.to.date( long in_date, long in_time, const string in_zone, const string out_zone, ref long out_date, ref long out_time )`

## Description
This converts a date and time in one time zone to the corresponding date and time in a different time zone.

## Arguments
| | | |
|---|---|---|
| `long` | `in_date` |  The date in the source time zone, specified as the number of days since 01-01-0001.  |
| `long` | `in_time` |  The time in the source time zone, specified as the number of seconds since 00:00 hour.  |
| `const string` | `in_zone` |  The source time zone.  |
| `const string` | `out_zone` |  The time zone to which the source date and time must be converted.  |
| `ref long` | `out_date` |  The number of days since 01-01-0001 in the target time zone.  |
| `ref long` | `out_time` |  The number of seconds since 00:00 hour in the target time zone.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
