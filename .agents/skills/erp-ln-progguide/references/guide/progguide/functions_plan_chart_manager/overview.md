# Plan Chart Manager overview
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated. Instead you should use the "Gantt And Schedule Charts" API.
The Plan Chart Manager is a graphical planning environment. You can use the Plan Chart Manager functions to develop applications that create and manipulate plan charts within this environment; the Plan Chart Manager acts as the server for the applications.

## Planning board
The Plan Chart Manager provides a planning board, on which you can build and maintain plan charts on line. Users can open sessions in order to define and modify activities, relations between activities, and so on. The planning board consists of:

- A time scale.

- Horizontal lines (the planning board lines), on which users can place activities.

- Columns that describe the activities.

## Activities and relations
Activities are the building blocks of a plan. An activity is an event or series of actions, with a start and end time. On the planning board, activities are displayed as horizontal bars whose length represents the duration of the activity. The relations between the activities constitute the planning structure.

## Time scale
You can define a different time unit for each plan, to be used in the time scale displayed at the top of the planning board. In principle, you can use any time unit, from a second to a year, as the base unit. In practice, day, week, and month are normally used, the day being the base unit. If required, you can define several time scales for each plan.

## Plan Chart Manager events
The Plan Chart Manager communicates with a client application by means of events. Each user action within the Plan Chart manager generates an event. The client must include a loop to handle these events.
The Plan Chart manager generates the following event types:
| | |
|---|---|
| PCM_EVTMENUSELECT | Occurs when the user selects a menu item of the planning board. |
| PCM_EVTPUSHBUTTON | Occurs when the user clicks on a button of the planning board. |
| PCM_EVTOBJECTPRESS | Occurs when the user clicks on an activity, relation, or marker on the planning board. |
| PCM_EVTOBJECTDPRESS | Occurs when the user double-clicks on an activity, relation, or marker. |
| PCM_EVTOBJECTMOVE | Occurs when the user moves an activity, relation, or marker. |
| PCM_EVTCLOSED | Occurs when the Plan Chart Manager is closed. |

## Colors
All colors must be composed by using the [rgb()](../functions_color/rgb.md) function. Or you can use one of the following predefined colors:
| | | |
|---|---|---|
| RGB.BLACK RGB.BLUE RGB.YELLOW | RGB.MAGENTA RGB.GREEN RGB.GRAY | RGB.RED RGB.WHITE RGB.CYAN |

## Related topics
- [Plan Chart Manager overview](overview.md)

- [Plan Chart Manager synopsis](synopsis.md)
