# get.time.zone()

## Syntax:
`function long get.time.zone( ref string time_zone() )`

## Description
Returns the current time zone. The program must supply a buffer of at least a size of 50 to store the result, otherwise the result is truncated.

## Arguments
| | | |
|---|---|---|
| `ref string` | `time_zone()` |  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
