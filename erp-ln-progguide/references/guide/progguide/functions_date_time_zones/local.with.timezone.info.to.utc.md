# local.with.timezone.info.to.utc()

## Syntax:
`function long local.with.timezone.info.to.utc( long local_days, long local_time, long utcdiff, ref domain ttutc utc )`

## Description
This converts a local date and time to [UTC](overview.md#utc) long format. For the conversion, it will NOT use the timezone of the user, but the difference in seconds to UTC as supplied in the variable utcdiff. Input values for local date and time must be in the signed 32-bit value range.

## Arguments
| | | |
|---|---|---|
| `long` | `local_days` |  A number of days since 01-01-0001.  |
| `long` | `local_time` |  A number of seconds since 00:00 hours.  |
| `long` | `utcdiff` |  The number of seconds this timezone should be considered away from UTC.  |
| `ref domain ttutc` | `utc` |  The UTC long format value corresponding to the specified local date and time.  |

## Return values
| | |
|---|---|
| 0 | Success. The supplied reference argument *utc* now contains the UTC value of the supplied local date and time. |
| -1 | Error. The exact result is negative or greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range. The supplied reference argument *utc* is unchanged. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
