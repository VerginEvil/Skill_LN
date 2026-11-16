# DsCmwindow

## Description
A main window (DsCmwindow) acts as the frame window for applications. It is used for starting processes and for creating graphical and character windows. Typically, a main window contains a border, title bar, control menu box, sizing controls, menu bar, toolbar, status bar, work area, and scroll bars.
A main window also acts as the frame window for modal and modeless dialog boxes.

## Events
A DsCmwindow object can generate the following events:
EVTKEYPRESS
EVTRESIZEWINDOW

## Attributes
| | | | |
|---|---|---|---|
| DsNbarMenu (long) | [CSG] | The object ID of the DsCbarMenu object to be displayed across the top of a main window, below the title bar. The menu bar becomes visible after this attribute is set. |  |
| DsNclose (long) | [CG] | Specifies whether or not the menu of a dialog window includes the Close command. It also controls the processing of ALT+F4. The default is TRUE. This attribute affects the window only if DsNdialog=TRUE. |  |
| DsNcmdStateList (long array) | [S] | Use to change the state of toolbar buttons and menu items. The array consists of one or more pairs of values. Each pair consists of the command ID of a toolbar button or menu item and the new state of the item. The possible values for the command state are: DSCMDNORMALResets the command/button to its default state. DSCMDDISABLED Disables the command/button. DSCMDCHECKED Sets the command/button to its checked state (you can combine this with either of the other options). |  |
| DsNcommandStrings (void data) | [CS] | The status field strings and tooltip strings for commands/buttons defined in DsCbarMenu and DsCtoolBar objects. The DsNcommandStrings data consists of a header followed by multiple entries that specify the required strings. The header contains two longs, one specifying the version number (currently always 1), the other specifying the number of following entries. Each entry consists of a long and two strings. The long contains the unique command ID. The strings contain the status bar text and the tooltip text respectively. |  |
| DsNdialog (long) | [CG] | Specifies whether or not the window is a dialog-type window. The default is FALSE. This attribute is often used in combination with DsNmodal. |  |
| DsNeventMask (long) | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks. |  |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |  |
| DsNhelpButton (boolean) | [CG] | Use to specify whether or not a main window of dialog type (DsNdialog = TRUE) contains a help button in the title bar. This button provides context-sensitive help. The default is TRUE. |  |
| DsNiconic (long) | [C] | Specifies whether or not the main window is realized as an icon (that is, minimized). The default is FALSE. |  |
| DsNinferiorPointerCursor (long) | [CSG] | The shape of the inferior mouse pointer when positioned over the main window. A child of a main window inherits this mouse pointer, unless otherwise specified. This attribute is overruled by a DsNsuperiorPointerCursor attribute set for the window itself or for ancestor windows. It is also overruled by a DsNinferiorPointerCursor setting in descendant windows. Possible values are: DSCDEFAULT (default) DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP |  |
| DsNmaxHeight (long) | [CSG] | The maximum height (in pixels) of the main window. |  |
| DsNmaxWidth (long) | [CSG] | The maximum width (in pixels) of the main window. |  |
| DsNminHeight (long) | [CSG] | The minimum height (in pixels) of the main window. |  |
| DsNminWidth (long) | [CSG] | The minimum width (in pixels) of the main window. |  |
| DsNmodal (long) | [CG] | This specifies whether the main window is modal or modeless. If TRUE, then the user must complete interaction with the window and close it before continuing with any further interaction outside the window. This attribute is normally used in combination with the DsNdialog attribute. The default is FALSE. |  |
| DsNobjectType (long) | [G] | The object type. |  |
| DsNparent (long) | [G] | The ID of the parent object. |  |
| DsNprocessGroup (long) | [CSG] | The ID of the process group to which events from the main window are sent. See [Processes, process groups, and main windows](../multitasking/processes_process_groups_and_main_windows.md). |  |
| DsNresizeable (long) | [CG] | Indicates whether or not the main window is resizable. The default is TRUE. |  |
| DsNsetState (long) | [CS] | The state of the object. This can also be set with the corresponding functions. Possible values are: DSMAP Makes object visible (see also [map.object()](map.object.md)). DSUNMAP Makes object invisible (see also [unmap.object()](unmap.object.md)). DSUPDATE (Re)draws the object (see also [update.object()](update.object.md)). DSRAISE Puts object in the forefront (see also [raise.object()](raise.object.md)). DSLOWER Puts object in the background (see also [lower.object()](lower.object.md)). DSCLEAR Destroys the gparts on a gwindow. DSSETSENSITIVE Makes object sensitive – that is the object is enabled (see also [set.sensitive()](set.sensitive.md)). DSSETINSENSITIVE Makes object insensitive – that is the object is disabled (see also [set.sensitive()](set.sensitive.md)). DSSETFOCUS Sets keyboard input focus on the object (see [set.focus()](set.focus.md)). DSUNSETFOCUS Moves keyboard input focus to the mwindow (see [unset.focus()](unset.focus.md)). Note that you cannot combine these values. |  |
| DsNstartHelpMode (boolean) | [S] | This indicates whether or not the window is in context-sensitive help mode (that is, whether or not SHIFT+F1 is enabled). |  |
| DsNsuperiorPointerCursor (long) | [CSG] | The shape of the superior mouse pointer when positioned over the main window. A child of a main window always inherits this mouse pointer. DsNsuperiorPointerCursor overrules any inferior mouse pointer (DsNinferiorPointerCursor) set for the window and all mouse pointers set for descendant windows. Possible values are: DSCDEFAULT DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP |  |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |  |
| DsNtitle (string) | [CS] | The title displayed in the title bar of the main window and as the caption for the window's icon. |  |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |  |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |  |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |  |
The following attributes are supported for backward compatibility only. Do not use them in new applications.
DsNcolumns DsNdata DsNdisplay DsNflags
DsNmaxColumnsDsNmaxRows DsNminRows DsNminColumns
DsNmode DsNrows DsNsize DsNwindow

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
