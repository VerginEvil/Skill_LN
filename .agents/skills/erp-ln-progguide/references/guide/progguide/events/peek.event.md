# peek.event()

## Syntax:
`function long peek.event( [ ref long event(EVTMAXSIZE) ] )`

## Description
This reads the event at the top of the event queue and stores it in *event*. It does not remove the event from the queue. If the event queue is empty, the function waits (that is, it is blocked) until an event arrives. To time out the *peek.event()* function, use set.timer()set.timer.

## Arguments
| | | |
|---|---|---|
| `[ ref long` | `event(EVTMAXSIZE) ]` |  Optional reference argument containing a long array in which the peek.event() function will write the [event array parameters](event_array_parameters.md).  |

## Return values
The event type. See [Event types](event_types.md).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long event(EVTMAXSIZE), object_id
select.event.input( object_id, EVTBUTTONPRESSMASK +
                EVTBUTTONRELEASEMASK + EVTKEYPRESSMASK +
EVTBUTTONMOTIONMASK )
while peek.event() = EVTBUTTONMOTION
                next.event( event )
                ....
endwhile
```

## Related topics
- [Events overview](overview.md)

- [Events synopsis](synopsis.md)

- [Event types](event_types.md)

- [Event array parameters](event_array_parameters.md)

- [Events sample program](sample_program.md)
