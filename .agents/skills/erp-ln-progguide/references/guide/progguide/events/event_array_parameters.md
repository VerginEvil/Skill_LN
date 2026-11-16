# Event array parameters
The event argument included in [next.event()](next.event.md), [peek.event()](peek.event.md), and [send.event()](send.event.md) consists of an array of type long containing a list of signed 32-bit integer values. Each value represents a detail of the incoming or outgoing event. You retrieve the contents of an event array by using the set of parameters defined for the particular event type. These parameters are listed below, by event type.

- [All events](#all_events)

- [Mouse button events:](#mouse_button_events)

- [Mouse motion events](#mouse_motion_events)

- [Keypress events](#key_press_events)

- [Window resize events](#window_resize_events)

- [Control button events](#control_button_events)

- [Field select events](#field_select_events)

- [Grid events](#grid_events)

- [List box item select events](#list_box_item_select_events)

- [Menu item select events](#menu_item_select_events)

- [Scrollbar select events](#scrollbar_events)

- [Tab frame events](#tab_frame_events)

- [Tree events](#tree_events)

- [Change focus events](#change_focus_events)

- [I/O events](#i_o_events)

- [OLE events](#ole_events)

- [Application termination events](#application_termination_events)

- [Help events](#events)

- [Client events](#client_events)

- [Bucket message events](#bucket_message_events)

- [Timer events](#timer_events)

## All events
| | |
|---|---|
| evt.type( *event*) | The [Event types](event_types.md). |
| evt.window( *event*) | The ID of the object that generated the event. |

## Mouse button events:
EVTBUTTONPRESS, EVTBUTTONDPRESS, and EVTBUTTONRELEASE
| | |
|---|---|
| evt.button.x( *event*) | X-position of mouse action in window. |
| evt.button.y( *event*) | Y-position of mouse action in window. |
| evt.button.state( *event*) | Indicates which modifier keys are held down when the mouse button is pressed. Possible values are: EVTSHIFTMASK EVTCONTROLMASK EVTBUTTON1MASK EVTBUTTON2MASK EVTBUTTON3MASK |
| evt.button.button( *event*) | Indicates which mouse button is pressed. Possible values are: EVTBUTTON1 left mouse button EVTBUTTON2 middle mouse button EVTBUTTON3 right mouse button |
| evt.button.rootx( *event*) | Absolute x-position of mouse action on desktop. |
| evt.button.rooty( *event*) | Absolute y-position of mouse action on desktop. |

## Mouse motion events
EVTBUTTONMOTION
| | |
|---|---|
| evt.motion.x( *event*) | X-position of mouse pointer in window during motion. |
| evt.motion.y( *event*) | Y-position of mouse pointer in window during motion. |
| evt.motion.state( *event*) | Indicates which modifier keys are held down while the mouse pointer is moved. Possible values are: EVTSHIFTMASK EVTCONTROLMASK EVTBUTTON1MASK EVTBUTTON2MASK EVTBUTTON3MASK |
| evt.motion.rootx( *event*) | Absolute x-position of mouse pointer on desktop during motion. |
| evt.motion.rooty( *event*) | Absolute y-position of mouse pointer on desktop during motion. |

## Keypress events
EVTKEYPRESS
| | |
|---|---|
| evt.keypress.key( *event*) | ASCII or TSS value of pressed key. |
| evt.keypress.state( *event*) | Indicates which modifier keys are held down while the key is being pressed. Possible values are: MOD_CTRL MOD_SHIFT MOD_ALT |

## Window resize events
EVTRESIZEWINDOW
| | |
|---|---|
| evt.resize.columns( *event*) | New width in number of columns (character window). |
| evt.resize.rows( *event*) | New height in number of rows (character window). |
| evt.resize.width( *event*) | New width in pixels (graphical window). |
| evt.resize.height( *event*) | New height in pixels (graphical window). |

## Control button events
EVTBUTTONSELECT
| | |
|---|---|
| evt.button.return( *event*) | Return value of the button, where relevant. |
| evt.button.checkstate( *event*) | The state of toolbar buttons, check boxes and option buttons. Possible values are: EVTBUTTONCHECKED button pressed or checked EVTBUTTONUNCHECKED button released or unchecked |

## Field select events
EVTFIELDSELECT
There are no parameters specific to these event types. See [All events](#all_events).

## Grid events
EVTGRIDEVENT
| | |
|---|---|
| evt.grid.row( *event*) | Row index (1-based index). |
| evt.grid.column( *event*) | Column index (1-based index). |
| evt.grid.width( *event*) | Column width. |
| evt.grid.height( *event*) | Row height. |
| evt.grid.range.left( *event*) | Index of leftmost column of range. |
| evt.grid.range.top( *event*) | Index of topmost row of range. |
| evt.grid.range.right( *event*) | Index of rightmost column of range. |
| evt.grid.range.bottom( *event*) | Index of bottommost row of range. |
| evt.grid.selmark( *event*) | Mark state of a selection. Possible values are: DSGRIDMARKNONE nothing marked DSGRIDMARKNEW new mark DSGRIDUNMARKunmark DSGRIDADDMARK add mark |
| evt.grid.reason( *event*) | The action that caused the event. Possible values are: |
| EVTGRIDCHANGEDATA | data changed |
| EVTGRIDCHANGEFOCUS | internal focus moved to another cell |
| EVTGRIDACTIVATE | selection activated by double-click |
| EVTGRIDFOCUSCHANGEDBYMOUSE | internal focus moved to another cell by mouse click |
| EVTGRIDMARKRANGE | range selected |
| EVTGRIDMARKCELL | cell selected |
| EVTGRIDMARKROW | row selected |
| EVTGRIDMARKCOLUMN | column selected |
| EVTGRIDRESIZEROW | row height changed |
| EVTGRIDRESIZECOLUMN | column width changed |
| EVTGRIDMOVEROW | row moved |
| EVTGRIDMOVECOLUMN | column moved |
| EVTGRIDBUTTONPRESS | control button pressed |
| EVTGRIDLISTBOXSELECT | item selected in list box |
| EVTGRIDRESETSELECTION | all rows, columns, cells unselected |
The value of the *evt.grid.reason* parameter determines which of the other parameters are included as part of the event. For example, if the event reason is EVTGRIDRESIZEROW, then *evt.grid.row* and *evt.grid.height* must be included in the event. Similarly, if the event reason is EVTGRIDMARKRANGE, then *evt.grid.range.left*, *evt.grid.range.top*, *evt.grid.range.right*, and *evt.grid.range.bottom* must be included in the event.

## List box item select events
EVTLISTBOXSELECT
| | |
|---|---|
| evt.listbox.item_id( *event*) | ID of the selected list-box item. |
| evt.listbox.reason( *event*) | The action that caused the event. Possible values are: EVTLISTBOXREASONTEXT text typed in edit field of combo box EVTLISTBOXREASONACTIVATE item double-clicked EVTLISTBOXREASONSELECTION selection changed |
| evt.listbox.selcount( *event*) | Number of selected items. |

## Menu item select events
EVTMENUSELECT
| | |
|---|---|
| evt.menu.return( *event*) | ID of the selected menu item. |

## Scrollbar select events
EVTSCROLLBARSELECT
| | |
|---|---|
| evt.scrollbar.action( *event*) | The action that caused the event. Possible values are: SBUP SBDOWN SBPRESS SBMOVE SBRELEASE SBPGUP SBPGDOWN SBHOME SBEND |
| evt.scrollbar.value( *event*) | Current position in scrollbar. |

## Tab frame events
EVTTABSELECT
| | |
|---|---|
| evt.tab.index( *event*) | Index of selected tab (1-based index) |

## Tree events
EVTTREESELECT
| | |
|---|---|
| evt.tree.item_id( *event*) | ID of the tree item that caused the event. |
| evt.tree.reason( *event*) | The action that caused the event. Possible values are: EVTTREEREASONACTIVATE leaf in tree activated EVTTREEREASONEXPAND tree node expanded EVTTREEREASONCOLLAPSE tree node collapsed EVTTREEREASONSELECT tree item selected |

## Change focus events
EVTCHANGEFOCUS and EVTSETFOCUS
| | |
|---|---|
| evt.focus.object( event ) | The object that currently has keyboard focus (EVTCHANGEFOCUS). The object that has received keyboard focus (EVTSETFOCUS). |
| evt.focus.key( event ) | Indicates the key that caused an EVTCHANGEFOCUS event. Possible values are: KEY_TAB KEY_BACKTAB KEY_UP KEY_DOWN KEY_RIGHT KEY_LEFT KEY_HOME KEY_END KEY_PGUP KEY_PGDOWN |

## I/O events
EVTIOEVENT
| | |
|---|---|
| event.array(1) | The event type. This is always EVTIOEVENT. |
| event.array(2) | The reason that the event was sent. Possible values are: |
| EVTSOCKHASDATA | data is available on the socket specified in event.array(3) |
| EVTSOCKIOERROR | error occurred on the socket specified in event.array(3) |
| EVTCONNECTREQUEST | connection request is pending on the socket specified in event.array(3) |
| event.array(3) | The file pointer of the relevant socket. |

## OLE events
EVTOLEEVENT
| | | | |
|---|---|---|---|
| evt.ole.event( *event*) | The OLE event type. Possible values are: |  |  |
|  |  | EVTOLECREATEINSTANCE EVTOLESETHOSTNAMES EVTOLESHOWWINDOW EVTOLEHIDEWINDOW EVTOLELOADDATA EVTOLESAVEDATA EVTOLECLOSE EVTOLELOCKSERVER EVTOLEUNLOCKSERVER EVTOLEDATACHANGED EVTOLERELEASED EVTOLEAUTOMATION EVTOLESHOWOBJECT EVTOLEOBJECTWINDOWVISIBLE EVTOLEOBJECTWINDOWINVISIBLE | class factory wants to create an object request hostnames request to make object visible request to make object invisible request to load an embedded object with data request to save an embedded object server closes embedded object set lock to keep application running reset lock embedded object data has changed all references to object released automation request to call DLL function request to scroll embedded object in view object in running mode object not in running mode |
|  | evt.ole.size( *event*) | For a data change or data save event, this stores the size of the data. |  |
|  | evt.ole.subobject( *event*) | If the OLE object is an embedded object, displayed in a graphical window (DsCgwindow), this indicates the ID of the graphical subobject in the gwindow. |  |

## Application termination events
EVTTERMINATION
| | |
|---|---|
| evt.termination.reason( *event*) | The action that caused the event. Possible values are: DSTerminationSetDir DSTerminationOpenStdin DSTerminationOpenStdout DSTerminationOpenStderr DSTerminationCreateProcess DSTerminationCreateThread DSTerminationNormalExit |
| evt.termination.exitcode( *event*) | The application’s exit code. |

## Help events
EVTHELPEVENT
| | |
|---|---|
| evt.help.return( *event*) | Return value of the control button, toolbar button, or menu option for which help is requested. This is -1 for all other object types. |
| evt.help.row( *event*) | Grid row index if help requested for a grid object. This is -1 for all other object types. |
| evt.help.column( *event*) | Grid column index if help requested for a grid object. This is -1 for all other object types. |
| evt.help.reason( *event*) | EVTHELPCOMMAND help requested using F1 EVTHELPCONTEXT help in context-sensitive help mode |

## Client events
EVTCLIENTMESSAGE
| | |
|---|---|
| evt.client.sender( *event*) | Process ID of sender. |
| evt.client.command( *event*) | Application-specific command code. |
| evt.client.argument( *event*) | Application-specific argument. |

## Bucket message events
EVTBUCKETMESSAGE
| | |
|---|---|
| evt.bms.sender( *event*) | Process ID of sender. |
| evt.bms.command( *event*) | Application-specific command code. |
| evt.bms.argument( *event*) | Application-specific argument. |

## Timer events
EVTTIMEREVENT
| | |
|---|---|
| evt.timer.id( *event*) | ID of timer that sent the event. |

## Related topics
- [Events overview](overview.md)

- [Events synopsis](synopsis.md)

- [Event types](event_types.md)

- [Event array parameters](event_array_parameters.md)

- [Events sample program](sample_program.md)
