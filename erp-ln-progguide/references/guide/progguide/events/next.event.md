# next.event()

## Syntax:
`function long next.event( [ ref long event(EVTMAXSIZE) ] )`

## Description
This removes the event at the top of the event queue and stores it in *event*. If the event queue is empty, the function waits (that is, it is blocked) until an event arrives. To time out the *next.event()* function, use set.timer()set.timer.
Note that events are sent to a *Process Group* and not to a process. In order to receive events to a process a call to the function *set.pgrp(pid, pid)* will create a process group for the current process. See [set.pgrp()](../functions_process_groups/set.pgrp.md)
The best way to trace next.event() related problems is to use on the command link of the bshell the following options: -dbgflow -dbgfun -tracelevel 1 -dbgmulact -keeplog -logfile a.file.name.

## Arguments
| | | |
|---|---|---|
| `[ ref long` | `event(EVTMAXSIZE) ]` |  Optional reference argument containing a long array in which the next.event() function will write the [event array parameters](event_array_parameters.md).  |

## Return values
The event type. See [Event types](event_types.md).

## Context
This function is implemented in the porting set and can be used in all script types.
Notes  Be careful in using next.event in WebUI and LN UI, only use it in combination with tc.ignore.process

## Example
```

long event(EVTMAXSIZE), object_id
select.event.input( object_id, EVTBUTTONPRESSMASK +
                EVTBUTTONRELEASEMASK + EVTKEYPRESSMASK +
EVTBUTTONMOTIONMASK )
next.event( event )
on case evt.type( event )
case EVTBUTTONPRESS:
                ...
case EVTKEYPRESS:
                ...
default:
                ...
endcase
```

## Related topics
- [Events overview](overview.md)
- [Events synopsis](synopsis.md)
- [Event types](event_types.md)
- [Event array parameters](event_array_parameters.md)
- [Events sample program](sample_program.md)
