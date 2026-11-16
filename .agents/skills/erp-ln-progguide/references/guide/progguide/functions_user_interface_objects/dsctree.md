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
| | | |
|---|---|---|
| Move between items | *A single item at a time* | <Arrow Up>, <Arrow Down> |
|  | *One scroll page at a time* | <PageUp>, <PageDown> |
|  | *To first and last items* | <Home>, <End> |
|  | *To next item whose label begins with a particular character* | Press key corresponding to the character |
| Expand/collapse nodes |  | <Arrow Right>, <Arrow Left> |
| Activate a leaf |  | <Enter> |
All the above mouse and keyboard actions generate an EVTTREESELECT event (see [Event types](../events/event_types.md)). Pressing any key other than those mentioned above generates an EVTKEYPRESS event.

## Events
A DsCtree object can generate the following events:
EVTTREESELECT
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTHELP

## Attributes
| | | |
|---|---|---|
| long | The ID of a tree node or leaf |  |
| long | The state of the specified node or leaf: |  |
|  | DSTREEEXPAND | Expands the node by one level |
|  | DSTREECOLLAPSE | Collapses the node if it is expanded |
|  | DSTREEREMOVE | Removes the item(if it is a node, all its children are also removed) |
|  | DSTREEEXPANDALL | Expands the node and all its children |
| | |
|---|---|
| DSOPENAGAIN | When reopening node, restore previous state. |
| DSOPENNONE | When reopening node, collapse all subnodes. |
| | |
|---|---|
| long | Version number (currently always 1). |
| long | Number of image sets used by the tree images. |
| long | Number of items in the tree. |
*Zero or more entries specifying the image sets used by the tree items.*
Normally, tree items of the same type use the same icon. This icon can have a different appearance in different situations – for example, when the item is selected, not selected, expanded, collapsed, and so on. An image set is the set of such images for a particular type of item.
For example, on the contents page of a Windows help file, the following icons represent a collapsed book and an expanded book respectively.
The two icons represent the image set for book-type items.
An image set entry contains the following fields:
| | |
|---|---|
| short | The image set ID |
| long | The ID of the image for items not selected and not expanded |
| long | The ID of the image for items selected but not expanded. If this is 0, the default is the ID of the image for images not selected and not expanded. |
| long | The ID of the image for nodes expanded but not selected. If this is 0, the default is the ID of the image for items not selected and not expanded. This is relevant only ot node items. |
| long | The ID of the image for nodes selected and expanded. If this is 0, the default is the ID of the image for items selected but not expanded. This is relevant only to node items. |
*Zero or more item entries containing the following fields:* byte The item type. Possible values are:
| | |
|---|---|
| 0 | leaf |
| 1 | node |
| 2 | sibling leaf |
| 3 | sibling node |
When changing the property of a tree item with *change.object()*, you must specify the full data for that item in the DsNtreeData attribute. In the case of a node, it is not necessary to redefine the node's children.

## Examples
The following is an example of DsNtreeData data used to create a new tree control:

## Resulting tree control

## DsNtreeData header
| | | |
|---|---|---|
| Version | Count (image sets) | Count (nodes) |
| 1 | 2 | 9 |

## DsNtreeData image set entries
| | | | | |
|---|---|---|---|---|
| Image set ID | Image ID (not selected, not expanded | Image ID (selected, not expanded) | Image ID (not selected, expanded) | Image ID (selected, expanded) |
| ID_FOLDER_SET | ID_FOLDER_1 | 0 | ID_FOLDER_2 | 0 |
| ID_SESSION_SET | ID_SESSION_1 | ID_SESSION_2 | 0 | 0 |

## DsNtreeData item entries
| | | | | |
|---|---|---|---|---|
| Type | Text | Image set ID | ID | Parent ID |
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
