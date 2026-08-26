# date.num()

## Syntax:
`function long date.num( )`

## Description
This returns the number of days from 01-01-0001 to the system date.
The applicable timezone can be found with the function [get.time.zone()](get.time.zone.md).

## Return values
| | |
|---|---|
| >= 0 | The number of days from 01-01-0001 to the system date. |
| -1 | Error. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Dates, times, time zones synopsis](synopsis.md)
- [Dates, times, time zones overview](overview.md)
