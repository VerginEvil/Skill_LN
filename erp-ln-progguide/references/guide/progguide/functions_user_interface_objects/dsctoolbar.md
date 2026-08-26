# DsCtoolBar

## Description
A DsCtoolBar object defines a toolbar for a main window (DsCmwindow). An application creates the entire toolbar with a single *create.object()* call. Subsequently, it can use *change.object()* toadd, remove, change, enable, and disable toolbar buttons.
Use the DsNcommandStrings attribute of the main window to specify status field and tooltip text for the toolbar buttons.

## Events
A DsCtoolBar object can generate the following event:
EVTBUTTONSELECT

## Attributes
| | | |
|---|---|---|
|  DsNbutton (long)  | [SQ] | Selects a particular toolbar button. The value specified is an index into the toolbar button list (1 based index) – separators are not counted. |
|  DsNbuttonState (long)  | [SQ] |  The state of the toolbar button identified by DsNbutton. Possible values are: DSTBBTNDISABLEDUNCHECKED DSTBBTNDISABLEDCHECKED (DSCHECK buttons only) DSTBBTNENABLEDUNCHECKED (default) DSTBBTNENABLEDCHECKED (DSCHECK buttons only)  |
|  DsNcommandList (long array)  | [C] |  The list of the command identifiers associated with the toolbar buttons. This attribute is mandatory when creating a toolbar. The command identifiers must be in the range 0 to 12287. The number of entries in the DsNcommandList array must equal the number of entries in the DsNimageList array (excluding separator entries). The event generated when a user clicks a toolbar button contains the command ID for the button.  |
|  DsNdockable (boolean)  | [CG] | Specifies whether a toolbar is dockable or fixed. When this attribute is FALSE, the toolbar is fixed at the top of the main window immediately below the menu bar. When TRUE (default), the toolbar is dockable; DsNgravity specifies its initial position.  |
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNgravity (long)  | [CG] |  The initial position and state of a dockable toolbar. Possible values are: DSTBTOP Docked at top of main window (default). DSTBBOTTOM Docked at bottom of main window. DSTBLEFT Docked at left of main window. DSTBRIGHT Docked at right of main window. DSTBFLOATING Floating toolbar, initially centered in main window. DSTBINVISIBLE Toolbar not visible (not valid in *create.object()*).  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNimageList (long array)  | [CSG] | The list of DsCpixmap objects and separators that the toolbar displays. This is a mandatory attribute for *create.object()*. A toolbar separator is indicated by a value of -1. All toolbar images must have the same width and height. The recommended size is 16 pixels wide and 15 pixels high.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstateList (long array)  | [CS] |  The state of the toolbar buttons. The array consists of one or more pairs of values. The first value in each pair is the button index (1-based index). The second value defines the state of the button. Possible state values are: DSTBBTNDISABLEDUNCHECKED DSTBBTNDISABLEDCHECKED (DSCHECK buttons only) DSTBBTNENABLEDUNCHECKED (default) DSTBBTNENABLEDCHECKED (DSCHECK buttons only)  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNtitle (string)  | [CS] | The title of the window of a floating toolbar. The default is an empty string.  |
|  DsNtypeList (long array)  | [C] |  The button types. The array consists of one or more pairs of values. The first value in each pair is the button index (1-based index). The second value defines the button type. Possible values are: DSNORMAL Normal pushbutton (default). DSCHECK A two-state button.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
