# date.to.utc()

## Syntax:
`function domain ttutc date.to.utc( long yearno, long monthno, long month_dayno, long hours, long minutes, long seconds )`

## Description
This converts the specified local date and time to UTC long format. Input values must be in the signed 32-bit value range.

## Arguments
| | | |
|---|---|---|
| `long` | `yearno` |  |
| `long` | `monthno` |  |
| `long` | `month_dayno` |  |
| `long` | `hours` |  |
| `long` | `minutes` |  |
| `long` | `seconds` |  |

## Return values
| | |
|---|---|
| >= 0 | The UTC long format value. |
| -1 | Error. The exact result is negative or greater than the maximum value 2^( BitCountOfLong-1) - 1 of the signed BitCountOfLong-bit range.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

long utc
utc = date.to.utc( 1991, 04, 20, 23, 12, 45 )
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
