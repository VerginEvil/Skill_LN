# suspend()

## Syntax:
`function void suspend( long msec )`

## Description
This stops execution of the current process for a specified number of milliseconds. You can specify any number of milliseconds in the range 0 to 2147483647 (the maximum value for a long).

## Arguments
| | | |
|---|---|---|
| `long` | `msec` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  Do not confuse this function with the [sleep()](sleep.md) function. The latter puts another process in a sleeping state until it is reactivated with the [reactivate()](reactivate.md) command.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
