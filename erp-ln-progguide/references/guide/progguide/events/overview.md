# Events overview
Use these functions for handling events.
Event-driven programs, such as BAAN 3GL scripts, are designed to respond to events. Usually, they consist of a main loop that waits for events to occur. When an event occurs, the program performs the appropriate actions to process the event. It then returns to its waiting state.
Most of the events that occur in a BAAN application relate to user interaction. When a user performs an action in the user interface (for example, clicking the mouse or pressing a keyboard key), this generates an event. The event consists of a package of information about the particular action. It is delivered to the event queue of the relevant process group and from there to the individual process that will handle the event. When the process retrieves the event from the event queue, it executes the piece of code appropriate for processing the particular type of event received.
Note that the event package takes the form of an array of signed 32-bit integer values, the so-called [event array parameters](event_array_parameters.md). You retrieve the individual items of information in the array by using a set of parameters specific to the event type.
The event paradigm is used in both ASCII and graphical programming environments. But some events are relevant only in graphical environments (for example, mouse events).
For further information on user interface controls and process groups, see [User interface objects overview](../functions_user_interface_objects/overview.md) and [Processes, process groups, and main windows](../multitasking/processes_process_groups_and_main_windows.md).

## Related topics
- [Events synopsis](synopsis.md)
- [Event types](event_types.md)
- [Event array parameters](event_array_parameters.md)
- [Events sample program](sample_program.md)
