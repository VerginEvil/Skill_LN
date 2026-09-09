# date.with.timezone.info.to.utc()

## Syntax:
`function domain ttutc date.with.timezone.info.to.utc( long yearno, long monthno, long month_dayno, long hours, long minutes, long seconds, long utcdiff )`

## Description
This converts the specified local date and time to [UTC](overview.md#utc) long format. For this conversion it will NOT use the timezone of the user, but the difference in seconds to UTC as supplied in the variable utcdiff. Input values must be in the signed 32-bit value range.

## Arguments
| | | |
|---|---|---|
| `long` | `yearno` |    |
| `long` | `monthno` |    |
| `long` | `month_dayno` |    |
| `long` | `hours` |    |
| `long` | `minutes` |    |
| `long` | `seconds` |    |
| `long` | `utcdiff` |    |

## Return values
| | |
|---|---|
| >= 0 | The UTC long format value. |
| -1 | Error. The exact result is negative or greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

long utc
utc = date.with.timezone.info.to.utc( 2003, 04, 18, 16, 20, 45,
7200 )
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
