# set.timer()

## Syntax:
`function long set.timer( long msec )`

## Description
This starts a timer that sends an EVTTIMEREVENT event to the calling process every *msec* milliseconds. The timer continues to send events until the process ends or until the program explicitly terminates the timer using [kill.timer()](kill.timer.md).

## Arguments
| | | |
|---|---|---|
| `long` | `msec` |  |

## Return values
A unique identifier for the timer.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  The [kill.timer()](kill.timer.md) function uses the identifiers returned by this function to specify which timer it is terminating.

## Example
```

tim.id = set.timer(2000)
next.event( event )
on case evt.type( event )
        case EVTTIMEREVENT:
                if (evt.timer.id(event) = tim.id )
                        message("My '2000' timer expired")
                endif
                break
        endcase
```

## Related topics
- [Events overview](../events/overview.md)
- [Timers overview and synopsis](overview_and_synopsis.md)
