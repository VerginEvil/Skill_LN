# utc.add()

## Syntax:
`function long utc.add( long i.utc, long year, long month, long day, long hour, long minute, long second, long o.utc )`

## Description
This adds years, months, days, hours, minutes, seconds to the input [UTC](overview.md#utc) value and makes corrections if necessary.
It processes the parameters from bigger to smaller units:

- First adds only years and the date is corrected (if started from a leap year)

- Than the months are added and the date is corrected to an existing one.

- The addition of days follow, and the result is so far the same hour, minutes, as it was in the beginning in the actual time-zone.

- Finally the hours, minutes, seconds are added.

## Arguments
| | | |
|---|---|---|
| `long` | `i.utc` |    |
| `long` | `year` |    |
| `long` | `month` |    |
| `long` | `day` |    |
| `long` | `hour` |    |
| `long` | `minute` |    |
| `long` | `second` |    |
| `long` | `o.utc` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| 1 | Best guess. |
| 2 | Failure. For example: Any intermediate result involves a date before the year 1 or past the year 9999. Any intermediate result or the final result of the addition is negative or greater than the maximum value 2^( [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-1) - 1 of the signed [BitCountOfLong](../3gl_features/data_types.md#BitCountOfLong)-bit range. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
This example shows the addition of days and hours across winter/summertime change
```

    in_utc = date.to.utc(2002,3,29,13,30,0)

    res = utc.add( in_utc, 0, 0, 1, 24, 0, 0, ou_utc )
```
The result in timezone "Europe/Amsterdam" is: ou_utc=1017577800, res = 0 (that is 2002.3.31 14:30:00)
This example shows the addition of days across winter/summertime change
```

    in_utc = date.to.utc(2002,3,29,13,30,0)

    res = utc.add( in_utc, 0, 0, 2, 0, 0, 0, ou_utc )
```
The result in timezone "Europe/Amsterdam" is: ou_utc=1017574200, res = 0 (that is 2002.3.31 13:30:00)
This example shows the substraction of 1 month from March 31st, 2000.
```

        in_utc = date.to.utc(2000,3,31,9,0,0)

        res = utc.add( in_utc, 0, -1, 0, 0, 0, 0, ou_utc )
```
The result in timezone "Europe/Amsterdam" is: ou_utc=951811200, res = 1 (that is 2000.2.29 9:0:0)

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
