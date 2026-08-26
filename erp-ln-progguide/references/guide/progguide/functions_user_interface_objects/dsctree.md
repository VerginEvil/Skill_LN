# DsCtree

## Description
A DsCtree object defines a tree view control. Like any tree view control, it displays a list of items as an indented outline that reflects the hierarchical relationship between the items.
Items in a tree control have a parent-child relationship. They can be either nodes or leaves. Nodes represent category headings and can have leaves and other nodes as children. Leaves do not have children. All items, except the root node, have one parent node; the root node is the highest node in the tree.
Each item in a tree control consists of an icon and a text label. If a node has children, it is preceded by a + or - button that enables the user to expand or collapse it respectively.
Each item has a unique ID. An item also has a parent ID; this is the ID of the item's parent node. An item can also have a sibling ID; this is the ID of the item that appears immediately below it within the same parent node. The parent and sibling IDs of an item determine where the item is positioned within the tree structure.
You use the DsNtreeData attribute to define the type, label, ID, image, and parent or sibling ID of a tree control item. You also use DsNtreeData to change the properties of a tree control item, by calling *change.object()* and defining the new properties in the DsNtreeData attribute.
For example, you can reposition an item within the tree control by specifying a different parent or sibling for the item. You cannot, however, change the parent ID of an item to 0 (because a tree control can have only one root node). Nor can you change an item's parent ID to that of one of the item's descendants or to the item's own ID. You can change a leaf to a node and vice versa – however, if you change a node to a leaf, all children of the node are automatically removed. You cannot change the unique ID of an item directly. To assign a new ID to an item, you must remove the item and then redefine it with the new ID. Note that when an item has been removed, you can reuse its ID for a new item.

## Navigation
Users can use the mouse or keyboard keys to navigate through a tree control and to activate items.

## Mouse actions
To move to an item with the mouse, click on the item. To activate an item, and to expand and collapse a node, double-click on it.

## Keyboard actions
Move between items *A single item at a time* UP ARROW, DOWN ARROW
*One scroll page at a time* Pg Up, Pg Dn
*To first and last items* HOME, END
*To move to next item whose label begins with a particular character* Press key correspoding to the character
Expand/collapse nodes RIGHT ARROW, LEFT ARROW
Activate a leaf ENTER
All the above mouse and keyboard actions generate an EVTTREESELECT event (see [Event types](../events/event_types.md)). Pressing any key other than those mentioned above generates an EVTKEYPRESS event.

## Events
A DsCtree object can generate the following events:
EVTTREESELECT
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTHELP

## Attributes
**
**
**
| | | |
|---|---|---|
|  DsNcommandList (long array)  | [CS] |  Use this to set the state of tree control items and to remove tree items. The array contains one or more entries in the following format:  |
|  DsNeventMask (long)  | [CSG] |  Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNeventReasonMask (long)  | [CSG] |  The EVTTREESELECT event can be generated when a tree item is activated, expanded, collapsed, or selected. The DsNeventReasonMask attribute specifies for which of these actions or reasons the event is generated. If a particular reason is not set in this attribute, then an event is not generated for that reason. Possible values are: EVTTREEREASONACTIVATEMASK EVTTREEREASONEXPANDMASK EVTTREEREASONCOLLAPSEMASK EVTTREEREASONSELECTMASK Use the bitwise OR operator to combine some or all of these flags.  |
|  DsNheight (long)  | [CSG] | The height of the scroll view window, in pixels. When the tree is longer than the window, a vertical scroll bar is automatically enabled.  |
|  DsNmode (long)  | [CSG] |  The tree mode. Possible values are:  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
| DsNselectedId | [CSG] | Specifies the ID of the currently selected tree item.  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
| DsNtreeData | [CS] |  This contains the tree data. The data consists of the following information: *A header containing the following fields:*  |
|  DsNwidth (long)  | [CSG] | The width of the scroll view window, in pixels. When the tree is wider than the window, a horizonotal scroll bar is automatically enabled.  |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Examples
The following is an example of DsNtreeData data used to create a new tree control:

## Resulting tree control

## DsNtreeData header
| | | |
|---|---|---|
| Version | Count (image sets)  | Count (nodes)  |
| 1 | 2 | 9 |

## DsNtreeData image set entries
| | | | | |
|---|---|---|---|---|
| Image set ID |  Image ID (not selected, not expanded  |  Image ID (selected, not expanded)  |  Image ID (not selected, expanded)  |  Image ID (selected, expanded)  |
| ID_FOLDER_SET | ID_FOLDER_1 | 0 | ID_FOLDER_2 | 0 |
| ID_SESSION_SET | ID_SESSION_1 | ID_SESSION_2 | 0 | 0 |

## DsNtreeData item entries
| | | | | |
|---|---|---|---|---|
| Type | Text | Image set ID | ID | Parent ID  |
| 1 | root | ID_FOLDER_SET | 1 | 0 |
| 0 | leaf1 | ID_SESSION_SET | 2 | 1 |
| 0 | leaf2 | ID_SESSION_SET | 6 | 1 |
| 1 | node1 | ID_FOLDER_SET | 86 | 1 |
| 1 | node2 | ID_FOLDER_SET | 87 | 1 |
| 0 | leaf7 | ID_SESSION_SET | 88 | 1 |
| 0 | leaf8 | ID_SESSION_SET | 43 | 1 |
| 0 | leaf9 | ID_SESSION_SET | 78 | 1 |
| 1 | node4 | ID_FOLDER_SET | 361 | 1 |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
