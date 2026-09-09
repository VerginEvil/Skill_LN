# set.alarm()

## Syntax:
`function long set.alarm( long msec )`

## Description
This starts a timer that sends a single EVTTIMEREVENT event to the calling process after the number of milliseconds specified in the *msec* argument. The timer automatically ends after sending the event. The timer also ends automatically when the process ends or when the program explicitly kills it with [kill.timer()](kill.timer.md).

## Arguments
| | | |
|---|---|---|
| `long` | `msec` |    |

## Return values
A unique identifier for the timer.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  The [kill.timer()](kill.timer.md) function uses the identifiers returned by this function to specify which timer it is terminating.

## Related topics
- [Events overview](../events/overview.md)

- [Timers overview and synopsis](overview_and_synopsis.md)
