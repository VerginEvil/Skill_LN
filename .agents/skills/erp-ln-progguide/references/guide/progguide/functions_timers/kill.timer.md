# kill.timer()

## Syntax:
`function void kill.timer( long timer_id )`

## Description
This ends a specified timer.

## Arguments
| | | |
|---|---|---|
| `long` | `timer_id` |    |

## Context
This function is implemented in the porting set and can be used in all script types.

## Argument
| | |
|---|---|
| timer_id | The timer identifier, as returned by [set.timer()](set.timer.md) or [set.alarm()](set.alarm.md) when the timer was created. |
Note  A timer automatically terminates when the process that started it ends.

## Related topics
- [Timers overview and synopsis](overview_and_synopsis.md)
