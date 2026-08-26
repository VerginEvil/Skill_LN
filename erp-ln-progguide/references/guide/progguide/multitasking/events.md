# Events
Infor Enterprise Server programs are designed to respond to events. Usually, they consist of a main loop that waits for events to occur. When an event occurs, the program performs the appropriate actions to process the event. It then returns to its waiting state.

## Event types
There are four broad categories of events, as listed below. For a full list of event types, see [Event types](../events/event_types.md).
- *User action events.* Most of the events that occur in a BAAN application relate to user interaction. When a user performs an action in the user interface (for example, clicking the mouse or pressing a keyboard key), this generates an event.
- *Timer events.* A process can start a timer that sends an event to the calling process at specified intervals. See [Timers overview and synopsis](../functions_timers/overview_and_synopsis.md).
- *Client events.* A process can send client events to another process by using the [send.event()](../events/send.event.md) function. The sending and receiving processes can determine their own protocol.
- *Bucket message events.* A process can broadcast bucket message events to other processes by using the [bms.send()](../functions_interprocess_communication_bshell/bms.send.md) function.   Note that functions such as [keyin$()](../functions_char_b_win/keyin.md) and [data.input()](../functions_char_b_win/data.input.md) are based internally on events.

## Event flow
When a UI object generates an event, the display server sends that event to the bshell. The bshell distributes received events to the event queues of the appropriate process groups; note that events are sent to process groups and not individual processes. The bshell never requests events; the display server always acts independently.
When one of the processes in the bshell requires input, the bshell checks whether any event is present in the event queue of the process group to which the process belongs. If there are no events in the event queue, it checks the connection between the bshell and the display server. If it finds events there, it distributes them to the appropriate process groups.

## Event masks
A process can set the event mask of a UI object in order to specify the types of events in which it is interested; the object then generates only events of these types (see [select.event.input()](../events/select.event.input.md)). Normally, event masks are automatically set for keyboard and mouse events. However, programmers should not assume any default settings for an event mask. Note that the following event types are always selected and cannot be masked: client events, timer events, bucket message events.

## Event functions
BAAN Tools provides the following functions for handling events:
- [next.event()](../events/next.event.md)
- [peek.event()](../events/peek.event.md)
- [pending.events()](../events/pending.events.md)
- [send.event()](../events/send.event.md)
- [select.event.input()](../events/select.event.input.md)

## Event arrays
The event argument included in the *next.event()*, *peek.event()*, and *send.event()* functions consists of an array of longs (of size EVTMAXSIZE) that contains details of the incoming or outgoing event. You retrieve the contents of an event array by using the set of parameters defined for the particular event type. See [Event array parameters](../events/event_array_parameters.md).

## Sample code
The following example illustrates the basic principle of event handling that is used by almost every event driven program.
```

#include <bic_event>

function main_event_loop()
{
        long event( EVTMAXSIZE )

        while next.event( event )
                on case evt.type( event )
                case EVTBUTTONPRESS:
                case EVTBUTTONRELEASE:
                        x = evt.button.x( event )
                        y = evt.button.y( event )
                        button = evt.button.button( event )
                        if button = EVTBUTTON1 then
                                print "left button pressed"
                                refresh()
                        endif
                        break
                default:
                        print "not a button press/release"
                        refresh()
                        return
                endcase
        endwhile
}
```

## Related topics
- [Multitasking and the GUI](multitasking_and_the_gui.md)
