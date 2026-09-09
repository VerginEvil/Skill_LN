# send.event()

## Syntax:
`function long send.event( long proc_grp, long event(EVTMAXSIZE) )`

## Description
This sends an event from the current process to the specified process group. It enables event-driven communication between processes. A process can send any event type using this function. Note that this is the only way to send events of type EVTCLIENTMESSAGE.
If the sending process requires an immediate response, use *suspend(0)* to force a context switch; that is, to force the system to give processor time to the destination process.

## Arguments
| | | |
|---|---|---|
| `long` | `proc_grp` |  The ID of the process group.  |
| `long` | `event(EVTMAXSIZE)` |  Long array containing the [event array parameters](event_array_parameters.md) of the event that must be sent to the process group.  |

## Return values
TRUE success
FALSE error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
This example sends a message that indicates the start of sending.
```

#define START_SEND      1
long process, event(EVTMAXSIZE)

evt.type( event )                                       =
EVTCLIENTMESSAGE
evt.client.sender( event )      = pid
evt.client.command( event )     = START_SEND

if not send.event( get.pgrp(process), event ) then
                message( "Process %d is not responding", process )
endif
```

## Related topics
- [Events overview](overview.md)

- [Events synopsis](synopsis.md)

- [Event types](event_types.md)

- [Event array parameters](event_array_parameters.md)

- [Events sample program](sample_program.md)
