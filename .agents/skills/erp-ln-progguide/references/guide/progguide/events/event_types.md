# Event types
The following section lists all available event types and describes their context.
| | |
|---|---|
| EVTBUTTONPRESS | Occurs when a mouse button is pressed. |
| EVTBUTTONDPRESS | Occurs when a mouse button is double pressed. |
| EVTBUTTONRELEASE | Occurs when a mouse button is released after being pressed. |
| EVTBUTTONMOTION | Occurs when the mouse is moved while at least one mouse button is pressed. |
| EVTKEYPRESS | Occurs when a keyboard key is pressed. |
| EVTRESIZEWINDOW | Occurs when a main window ( [DsCmwindow](../functions_user_interface_objects/dscmwindow.md)) is resized. |
| EVTBUTTONSELECT | Occurs when a control button is selected. Examples of control buttons are push buttons ( [DsCpushButton](../functions_user_interface_objects/dscpushbutton.md)), check boxes ( [DsCcheckBox](../functions_user_interface_objects/dsccheckbox.md)), option buttons ( [DsCradioButton](../functions_user_interface_objects/dscradiobutton.md)), toolbar buttons ( [DsCtoolBar](../functions_user_interface_objects/dsctoolbar.md)), and drawn buttons ( [DsCdrawnButton](../functions_user_interface_objects/dscdrawnbutton.md)). |
| EVTFIELDSELECT | Occurs when a new value is entered in an edit field ( [DsCfield](../functions_user_interface_objects/dscfield.md)). |
| EVTGRIDEVENT | Occurs when a grid control ( [DsCgrid](../functions_user_interface_objects/dscgrid.md)) is modified. |
| EVTLISTBOXSELECT | Occurs when one or more items are selected in a combo box ( [DsCcomBox, DsCdDComBox, DsClistBox, DsCdDListBox](../functions_user_interface_objects/dscboxxx.md)), a drop-down combo box ( [DsCcomBox, DsCdDComBox, DsClistBox, DsCdDListBox](../functions_user_interface_objects/dscboxxx.md)), a drop-down list box ( [DsCcomBox, DsCdDComBox, DsClistBox, DsCdDListBox](../functions_user_interface_objects/dscboxxx.md)), or a list box ( [DsCcomBox, DsCdDComBox, DsClistBox, DsCdDListBox](../functions_user_interface_objects/dscboxxx.md)). |
| EVTMENUSELECT | Occurs when a menu item is selected in a bar menu object ( [DsCbarMenu](../functions_user_interface_objects/dscbarmenu.md)). |
| EVTSCROLLBARSELECT | Occurs when a scrollbar ( [DsCscrollbar](../functions_user_interface_objects/dscscrollbar.md) or [DsCslider](../functions_user_interface_objects/dscslider.md)) is moved or selected. |
| EVTTABSELECT | Occurs when a tab is selected in a tab frame control ( [DsCtabFrame](../functions_user_interface_objects/dsctabframe.md)). |
| EVTTREESELECT | Occurs when an item in a tree control ( [DsCtree](../functions_user_interface_objects/dsctree.md)) is expanded, collapsed, or selected. |
| EVTCHANGEFOCUS | Occurs when the keyboard focus is moved. The user can move the focus from one object to another by pressing the TAB key or an arrow key. |
| EVTSETFOCUS | Occurs when an object receives keyboard focus by the user clicking on it with the mouse. |
| EVTIOEVENT | Occurs when data is available on a socket, when a connection request is pending on a socket, and when an I/O error occurs on a socket. |
| EVTOLEEVENT | Occurs when some action is performed on an OLE object in a graphical window ( [DsCgwindow](../functions_user_interface_objects/dscgwindow.md)). Only BAAN Windows can generate this event. |
| EVTTERMINATION | Occurs when a Windows application started by BAAN Windows (Notepad, for example) terminates. Only BAAN Windows can generate this event. |
| EVTHELPEVENT | Occurs in response to a request for help on a user interface object. |
| EVTBUCKETMESSAGE | Occurs when a process sends a bucket message, using bms.send()bms.send. |
| EVTCLIENTMESSAGE | Occurs when a process sends a client message, using [send.event()](send.event.md). |
| EVTTIMEREVENT | Occurs when a timer sends an event. |

## Related topics
- [Events overview](overview.md)

- [Events synopsis](synopsis.md)

- [Event types](event_types.md)

- [Event array parameters](event_array_parameters.md)

- [Events sample program](sample_program.md)
