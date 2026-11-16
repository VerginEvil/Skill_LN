# date.to.num()

## Syntax:
`function long date.to.num( long yearno, long monthno, long month_dayno )`

## Description
This returns the number of days since 01-01-0001 for a specified year, month, and day of the month.

## Arguments
| | | |
|---|---|---|
| `long` | `yearno` |    |
| `long` | `monthno` |    |
| `long` | `month_dayno` |    |

## Return values
| | |
|---|---|
| 0 | The number of days since 01-01-0001. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long no_of_days
no_of_days = date.to.num( 1991, 04, 20 ) | Returns 726942
```

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)

- [Dates, times, time zones overview](overview.md)
