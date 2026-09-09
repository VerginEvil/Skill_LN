# gbf.init()

## Syntax:
`#include <bic_gbf>`
`function long gbf.init( const string library(), const string title(), [ long default.menu, long default.button, long default.options, long standard.buttons, long default.context ] )`

## Description
This function must be the first to be called, it initializes the global data structures of the GBF. It is not forbidden to reactivate a new run of the GBF in a session after a previous run of the GBF has terminated, the GBF has to clear its global variables again. This cleaning of the global variables cannot be done when leaving the GBF as at that point in time it must still be possible to get some information about the settings in order for the application to save and restore some user preferences, see for example [gbf.get.refresh.strategy()](gbf.get.refresh.strategy.md) and [gbf.get.sort.strategy()](gbf.get.sort.strategy.md).

## Arguments
| | |
|---|---|
| Function | Mandatory or optional |
| gbf.drag.drop | Optional, but if not present, no drag and drop will be available |
| gbf.get.top.level | Mandatory |
| gbf.get.children | Optional, but then another function should be set with [gbf.set.child.function()](gbf.set.child.function.md) |
| gbf.help.selected | Optional, and another function may be set with [gbf.set.help.function()](gbf.set.help.function.md) |
| gbf.menu.selected | Optional, but then another function must be set with [gbf.set.menu.function()](gbf.set.menu.function.md) |
| | |
|---|---|
| prog.name | The program name as given by the global variable prog.name$ but this field will only be shown when the user has enabled the displaying of session codes in the titlebar |
| session.desc | The description of the program or session as obtained by the function call: tt.session.desc(prog.name$, …) |
| user.name | The name of the current user, as given by the global variable logname$ |
| | | |
|---|---|---|
| main menu flag | submenu flag | description |
| GBF.MENU.NONE |  | No default menu, not even a menu bar is created, so no custom menu headings or items can be added. Only keystrokes can be added. |
| GBF.MENU.BAR.ONLY |  | Create only an empty menu bar, so no standard menu is added, but allow for custom menu headings and items and keystrokes |
| GBF.MENU.FILE |  | *file* menu on menu bar |
|  | GBF.MENU.FILE.RFSH | *refresh* in submenu |
|  | GBF.MENU.FILE.OPEN | *open all* in submenu |
|  | GBF.MENU.FILE.READ | *read all* in submenu |
|  | GBF.MENU.FILE.PRNT | *print options…* and *print* in submenu |
|  | GBF.MENU.FILE.SAVE | *save* in submenu |
|  | GBF.MENU.FILE.QUIT | *save + exit* in submenu |
|  | GBF.MENU.FILE.EXIT | *exit program* in submenu |
|  | GBF.MENU.FILE.ALL | same as: GBF.MENU.FILE + GBF.MENU.FILE.RFSH + GBF.MENU.FILE.PRNT + GBF.MENU.FILE.EXIT |
| GBF.MENU.SRCH |  | *find* menu on menu title bar |
|  | GBF.MENU.SRCH.DESC | Search *by description…* in submenu |
|  | GBF.MENU.SRCH.CODE | Search *by code…* in submenu |
|  | GBF.MENU.SRCH.FRST | Search for *first* in submenu |
|  | GBF.MENU.SRCH.NEXT | Search for *next* in submenu |
|  | GBF.MENU.SRCH.PREV | Search for *previous* in submenu |
|  | GBF.MENU.SRCH.LAST | Search for *last* in submenu |
|  | GBF.MENU.SRCH.CURR | *Search in current set* submenu, which is the same as GBF.SEARCH.CURRENT search strategy (see gbf.set.search.strategy()) |
|  | GBF.MENU.SRCH.READ | *Read before search* submenu item, which is the same as GBF.SEARCH.ALL search strategy (see gbf.set.search.strategy()) |
|  | GBF.MENU.SRCH.INS | *Match case* submenu item. |
|  | GBF.MENU.SRCH.ALL | Same as: GBF.MENU.SRCH + GBF.MENU.SRCH.DESC + GBF.MENU.SRCH.CODE + GBF.MENU.SRCH.FRST + GBF.MENU.SRCH.NEXT + GBF.MENU.SRCH.PREV + GBF.MENU.SRCH.LAST + GBF.MENU.SRCH.CURR + GBF.MENU.SRCH.READ + GBF.MENU.SRCH.INS |
| GBF.MENU.SORT |  | *sort* menu on menu title bar |
|  | GBF.MENU.SORT.NONE | *none* sorting in submenu |
|  | GBF.MENU.SORT.DESC | sort *by description* in submenu |
|  | GBF.MENU.SORT.CODE | sort *by code* in submenu |
|  | GBF.MENU.SORT.ASC | sort *ascending* in submenu |
|  | GBF.MENU.SORT.DSC | sort *descending* in submenu |
|  | GBF.MENU.SORT.ALL | same as: GBF.MENU.SORT + GBF.MENU.SORT.NONE + GBF.MENU.SORT.DESC + GBF.MENU.SORT.CODE + GBF.MENU.SORT.ASC + GBF.MENU.SORT.DSC |
| GBF.MENU.HELP |  | *help* menu on menu bar |
|  | GBF.MENU.HELP.CONT | help on *contents* in submenu |
|  | GBF.MENU.HELP.SRCH | *what’s this ?* in submenu |
|  | GBF.MENU.HELP.GBF | *Color Descriptions…*, *Icon Descriptions…* and *using browser* in submenu |
|  | GBF.MENU.HELP.SESS | *using session* in submenu |
|  | GBF.MENU.HELP.ABOUT | *about…* in submenu |
|  | GBF.MENU.HELP.ALL | same as: GBF.MENU.HELP + GBF.MENU.HELP.CONT + GBF.MENU.HELP.SRCH + GBF.MENU.HELP.GBF + GBF.MENU.HELP.SESS + GBF.MENU.HELP.ABOUT |
| GBF.MENU.ALL |  | same as: GBF.MENU.FILE.ALL + GBF.MENU.SRCH.ALL + GBF.MENU.SORT.ALL + GBF.MENU.HELP.ALL |
Note that when the flag standard.button is given, then some more menu items may be added.
When no default.menu is given (so the gbf.init() is called with only 2 arguments) then the GBF.MENU.ALL flag is used as the current value for default.menu. It is required to have the main menu flag (once) as well as all submenu flags for those options that are wanted. When only specifying the submenu, it will not show up. It is advised to use the GBF.MENU.ALL flag as default.menu. Disabling of submenu items can also easily be accomplished by subtracting them from this default. For example if no printing is wanted then the default.menu could be given as: GBF.MENU.ALL – GBF.MENU.FILE.PRINT.
Also a whole menu can be disabled in this way. For example suppose sorting is not wanted, then give as the default.menu: GBF.MENU.ALL – GBF.MENU.SORT or GBF.MENU.ALL – GBF.MENU.SORT.ALL.
The original idea of the GBF was to have an object browser, which means more or less a read-only view on the objects. Updates on the object tree can only be done by the main application that is called on a menu selection or keystroke. This means that these updates, for example creating new objects or deleting old objects, should be done by the main application before the function [gbf.menu.selected()](gbf.menu.selected.md) returns from the main application back to the GBF. This mechanism ensures that the GBF always displays the information as it is in the database, that is, there is no need for a special save function. Nevertheless, it is possible to have Save and Save+Quit menus under the File menu heading. However, they must be specially be enabled, since they do not add up to the GBF.MENU.FILE.ALL or GBF.MENU.ALL, so the default.menu should be given as: GBF.MENU.ALL + GBF.MENU.FILE.SAVE + GBF.MENU.FILE.QUIT.
These Save and Save+Quit menu items will be insensitive (‘white’) when the save function
gbf.menu.selected()
could not be found in the given library.
Also the original idea of the GBF was to have a lazy read strategy, that is read only what needs to be shown (see also [gbf.start()](gbf.start.md) and gbf.set.search.strategy()). Nevertheless there are two non-standard menu entries:
| | | | |
|---|---|---|---|
| Menu identification | Menu text | Keystroke | Description |
| GBF.MENU.FILE.READ | Read All | Ctrl+R | read the whole object tree, do not change view |
| GBF.MENU.FILE.OPEN | Open All | Ctrl+O | open all interior nodes whose children have already been read |
By default, that is with the GBF.MENU.ALL or GBF.MENU.FILE.ALL these two options are excluded, so if they are wanted, they should be explicitly be included, so the default.menu should be given as: GBF.MENU.ALL + GBF.MENU.FILE.OPEN + GBF.MENU.FILE.READ
Note that when the open strategy (see: [gbf.get.open.strategy()](gbf.get.open.strategy.md) [gbf.set.open.strategy() *](gbf.set.open.md)) contains the GBF.OPEN.READALL option then it is advised to NOT use the GBF.MENU.FILE.READ.
The GBF.MENU.FILE.RFSH menu allows to refresh the contents of the GBF using the current refresh strategy as has been set by [gbf.set.refresh.strategy()](gbf.set.refresh.strategy.md). Also the sort menu will reflect the current sorting strategy as has been set by [gbf.set.sort.strategy()](gbf.set.sort.strategy.md) as well as the current selected sort strategy by the end user via the menu can be retrieved by the application using [gbf.get.sort.strategy()](gbf.get.sort.strategy.md).
If the library does not contain the [gbf.help.selected()](gbf.help.selected.md) function, then the help menu entries identified by GBF.MENU.HELP.CONT and GBF.MENU.HELP.SRCH will be insensitive (‘white’). When an help function is defined later on (see [gbf.set.help.function()](gbf.set.help.function.md)) these menu items will become selectable (‘black’).
| | |
|---|---|
| Button flag | Description (see also: submenu flag column in menu flag table above) |
| GBF.BUTTON.NONE | no button bar will be created |
| GBF.BUTTON.BAR.ONLY | create only an empty button bar, so no standard buttons are added, but allow for custom buttons |
| GBF.BUTTON.FILE.QUIT | same as: GBF.MENU.FILE.QUIT |
| GBF.BUTTON.FILE.EXIT | same as: GBF.MENU.FILE.EXIT |
| GBF.BUTTON.FILE.PRNT | same as: GBF.MENU.FILE.PRNT |
| GBF.BUTTON.FILE.SAVE | same as: GBF.MENU.FILE.SAVE |
| GBF.BUTTON.CUT | application defined CUT button |
| GBF.BUTTON.UNDO | application defined UNDO button |
| GBF.BUTTON.INSERT | application defined INSERT button |
| GBF.BUTTON.COPY | application defined COPY button |
| GBF.BUTTON.PASTE | application defined PASTE button |
| GBF.BUTTON.DELETE | application defined DELETE button |
| GBF.BUTTON.SRCH.DESC | same as: GBF.MENU.SRCH.DESC |
| GBF.BUTTON.FRST | same as: keystroke HOME |
| GBF.BUTTON.PREV | same as: keystroke PageDown |
| GBF.BUTTON.NEXT | same as: keystroke PageUp |
| GBF.BUTTON.LAST | same as: keystroke END |
| GBF.BUTTON.GRP.NEW | application defined NEW GROUP button |
| GBF.BUTTON.GRP.FRST | go to oldest brother of selected object |
| GBF.BUTTON.GRP.PREV | same as: Ctrl+UpArrow |
| GBF.BUTTON.GRP.NEXT | same as: Ctrl+DownArrow |
| GBF.BUTTON.GRP.LAST | go to youngest brother of selected object |
| GBF.BUTTON.TEXT | application defined TEXT button |
| GBF.BUTTON.HELP | same as: GBF.MENU.HELP |
| GBF.BUTTON.ALL | same as: GBF.BUTTON.FILE.PRNT + GBF.BUTTON.FILE.SAVE + GBF.BUTTON.UNDO + GBF.BUTTON.INSERT + GBF.BUTTON.COPY + GBF.BUTTON.DELETE + GBF.BUTTON.SRCH.DESC+ GBF.BUTTON.FRST + GBF.BUTTON.PREV + GBF.BUTTON.NEXT + GBF.BUTTON.LAST + GBF.BUTTON.GRP.NEW + GBF.BUTTON.GRP.FRST + GBF.BUTTON.GRP.PREV + GBF.BUTTON.GRP.NEXT + GBF.BUTTON.GRP.LAST + GBF.BUTTON.TEXT + GBF.BUTTON.HELP |
Note that if the flag standard.button is given, then that value is first added (actually: bitwise ‘or’-ed) to this default.button flag to get all the buttons displayed.
When no default.button is given (so the [gbf.init()](gbf.init.md) is called with only 2 or 3 arguments) then the GBF.BUTTON.ALL flag is used as the current value for the default.button
The position of the button bar in the GBF window is taken from the User Data (table ttaad200, session ttaad2500m000). The order of the buttons is hard coded in the GBF, but will follow as far as possible the standard Baan order of buttons. When a button in the above table is marked as: application defined, then the application can use this button on his own behalf. The GBF will create these buttons (if specified of course) and makes them insensitive, since the GBF does not handle these buttons. The application should connect these buttons to a menu item, that can be done via the function [gbf.set.menu.item()](gbf.set.menu.item.md) and setting the button mnemonic. This association will also enable the button.
It is recommended to use the following initial values for default.button:
GBF.BUTTON.ALL when a button bar is wanted
GBF.BUTTON.NONE when no button bar is wanted
| | |
|---|---|
| Option flag | Description |
| GBF.OPT.1.WINDOW | have one window |
| GBF.OPT.2.WINDOWS | Have 2 windows: left one for interior objects in tree format right one for leaf nodes in free format |
| GBF.OPT.NO.TREE.CONTROL | Use standard server based GBF drawing techniques |
| GBF.OPT.TREE.CONTROL | Use local windows Tree Control for drawing the actual tree |
| GBF.OPT.FONT.FIXED | Use default FixedFont for object descriptions |
| GBF.OPT.FONT.VARIABLE | Use default VariableFont for object descriptions |
| GBF.OPT.FONT.RUNTIME | Allow dynamic font changes, so add Font… menu entry to standard GBF File menu |
| GBF.OPT.NO.LABELS | Do not have the status bar at the bottom of the browser |
| GBF.OPT.1.LABEL | Have only 1 label in the status bar |
| GBF.OPT.2.LABELS | Have only 2 labels in the status bar |
| GBF.OPT.3.LABELS | Have only 3 labels in the status bar |
| GBF.OPT.4.LABELS | Have only 4 labels in the status bar |
| GBF.OPT.5.LABELS | Have all 5 labels in the status bar |
| GBF.OPT.CYCLE | Display cycles (with a red line) on the window |
| GBF.OPT.DRAG.DROP | Main application supports drag and drop (see [gbf.drag.drop()](gbf.drag.drop.md)) |
| GBF.OPT.SESSION.DRAG | Indicates that this GBF session, which should be a composite child session, supports dragging to other composite child sessions. (see [Composite Sessions overview](../functions_composite_sessions/overview.md)) When this option is set, the callback function [gbf.on.drag()](gbf.on.drag.md) must be implemented by the GBF application script. |
| GBF.OPT.MULTIPLE | Main application supports multiple select (see [gbf.menu.selected()](gbf.menu.selected.md)) |
| GBF.OPT.MULTI.ONSELECT | Function [gbf.on.selection()](gbf.on.selection.md) will be called with the expected number of selected objects returned by function [gbf.get.selected.nr()](gbf.get.selected.nr.md) after the actual selection has been done. Without this option function gbf.on.selection will be called on a multi select, however not with the expected number of selected objects. This behavior is kept the same as before. This option adds an extra call of gbf.on.selection at the end of the processing of the selection. This way the state of a command can be determined correctly in the function gbf.on.selection This option is LN UI only. This option is available from TIV level 2400 |
| GBF.OPT.PROGRESS | When doing a lot of nested reads (e.g. due to a “ Read before search”, “Read All” or “Open All”) then a progress bar (or progress indicator) will be used to display the progress. This progress bar will have a STOP button allowing you to stop further reading. See also [standard menu items and function keys](standard_menu_items_and_function_keys.md) during read. |
| GBF.OPT.NO.PROGRESS | No progress bar will ever be displayed |
| GBF.OPT.SHADOWS (Baan IV) | Draw shadow lines around the icons in the window, which make them look more like buttons. |
| GBF.OPT.FORCE.SHADOW (Baan V) |  |
| GBF.OPT.UNSELECT | Unselect item when it is selected again. If not specified, the tree will behave as in the Microsoft tree. |
| GBF.OPT.NO.UNSELECT | Keep item selected when it is selected again. |
| GBF.OPT.NO.POP.UP | GBF should not generate error pop-ups on some problems: 1. memory shortage 2. icons not found in icon groups |
| GBF.OPT.POP.UP | GBF should always generate error pop-ups on problems |
| GBF.OPT.DEBUG | GBF now gives some more debugging information, such as 1. Unrecognized keystrokes are displayed in label1 2. Popup when calling a GBF function when it is not allowed (GBF is in wrong state) 3. Popup and same text in label1 when trying to call an unimplemented call back function, that is [gbf.drag.drop()](gbf.drag.drop.md), [gbf.get.top.level()](gbf.get.top.level.md), [gbf.get.children()](gbf.get.children.md), [gbf.help.selected()](gbf.help.selected.md), or [gbf.menu.selected()](gbf.menu.selected.md) gbf.drag.drop()gbf.get.top.level()gbf.get.children()gbf.help.selected()gbf.menu.selected() 4. Popup on unexpected failures when issuing a main application call back 5. Popup when a main application function requests termination of the GBF (in general always directly followed by the next popup) 6. Popup when actually terminating the GBF on user request (in general always directly after the previous pop up) 7. Popup when adding a menu item with a keystroke which is handled differently by GBFgbf.set.menu.item (see gbf.set.menu.item() ) and ‘shift’ problem description). 8. Popup when gbf.add.object() is called with an illegal function identification, icon set or a too long description 9. The main window is immediately displayed when leaving this [gbf.init()](gbf.init.md) function. Otherwise displaying of the main window is postponed until the subsequent [gbf.start()](gbf.start.md) function call. Use this option only when developing the main application |
| GBF.OPT.NO.DEBUG | GBF does not give developing debug popups |
| GBF.OPT.DEFAULT | GBF.OPT.1.WINDOW + GBF.OPT.SHADOWS + GBF.OPT.CYCLE + GBF.OPT.5.LABELS + GBF.OPT.UNSELECT + GBF.OPT.POP.UP + GBF.OPT.PROGRESS + GBF.NO.TREE.CONTROL + GBF.OPT.NO.DEBUG |
It is recommended to use the GBF.OPT.DEFAULT value for default.options flag.
When no default.options is given (so the [gbf.init()](gbf.init.md) is called with at most 4 arguments) then the GBF.OPT.DEFAULT flag is used as the current value for default.options.
Note that the GBF does not start running yet. This means that the control still lies within the main application. The idea is that now other configuration functions are called by the application, such as:
· · adding new icons sets, see [gbf.set.resource()](gbf.set.resource.md) and [gbf.set.interior.icon()](gbf.set.interior.icon.md)
· · add menus and keystrokes, see [gbf.set.menu.function()](gbf.set.menu.function.md), gbf.add.menu.head() and [gbf.set.menu.item()](gbf.set.menu.item.md).
· · add new strategies to get child nodes, see gbf.add.child.function()
· · set the refresh policy, see [gbf.set.refresh.strategy()](gbf.set.refresh.strategy.md)
| | | | |
|---|---|---|---|
| Button flag | Menu heading | Menu item | Description |
| GBF.BUTTON.COPY | Edit | Copy | Copy the current selected object(s) |
| GBF.BUTTON.CUT | Edit | Cut | Cut (delete) the current selected object(s) |
| GBF.BUTTON.DELETE | Edit | Delete | Delete the current selected object(s) |
| GBF.BUTTON.GRP.NEW | Group | New | Insert a new group object |
| GBF.BUTTON.INSERT | File | New | Insert a new object |
| GBF.BUTTON.PASTE | Edit | Paste | Paste the contents of the cut/copy buffers into the current selected object |
| GBF.BUTTON.TEXT | Edit | Text | Start the text editor for the current selected object(s) |
| GBF.BUTTON.UNDO | Edit | Undo | Undo the last operation |
For the Cut and Copy operation the GBF will put the current selected object into the so called cutcopy buffers and the application can use this buffered information, see also [gbf.get.cutcopy.nr()](gbf.get.cutcopy.nr.md) and [gbf.get.cutcopy()](gbf.get.cutcopy.md). Note that on a Delete and Cut the application still has to tell the GBF that these objects should be deleted.
| | | | |
|---|---|---|---|
| context.menu flag | menu heading | menu item | description |
| GBF.BUTTON.COPY | Edit | Copy | Copy the current selected object(s) |
| GBF.BUTTON.CUT | Edit | Cut | Cut (delete) the current selected object(s) |
| GBF.BUTTON.DELETE | Edit | Delete | Delete the current selected object(s) |
| GBF.BUTTON.GRP.NEW | Group | New | Insert a new group object |
| GBF.BUTTON.INSERT | File | New | Insert a new object |
| GBF.BUTTON.PASTE | Edit | Paste | Paste the contents of the cut/copy buffers into the current selected object |
| GBF.BUTTON.TEXT | Edit | Text | Start the text editor for the current selected object(s) |
The GBF will not take over control. This means that the browser will not be started, until the subsequent [gbf.start()](gbf.start.md) function call.

## Return values
| | |
|---|---|
| 0 | Success |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.NO.GRAPHICS | GBF can only run on graphical displays, not on ASCII only displays |
| GBF.NO.MEMORY | Not enough memory |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
