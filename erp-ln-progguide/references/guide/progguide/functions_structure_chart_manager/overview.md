# Structure Chart Manager overview
*Deprecated.* This API is only supported for Baan Windows and its usage is therefore deprecated.
The Structure Chart Manager is a tool that displays graphical tree structures. The functions described in this section enable programmers to create tree structures and to subsequently change their attributes.
A tree structure displays a list of items as an indented outline that reflects the hierarchical relationship between the items. The items in the tree structure are referred to as nodes. The first node in the tree is referred to as the root node. Nodes in a tree structure have a parent-child relationship. Each node can have a number of child nodes, which are indented below it in the tree structure. Every node, except the root node, has a parent node – that is, the node under which it is indented.
Each node has a node ID, which is its sequence number in the sequence of child nodes associated with a particular parent. Each node, except the root node, also has a parent ID, which is the ID of its parent node. The parent and node IDs of a node determine where the item is positioned within the tree structure.
Nodes must be created from the top down. That is, the parent node must be present before you can create a child node for that parent.

## Interprocess communication (IPC)
Communication between the client program and the Structure Chart Manager is full-duplex. This means that the client can send information to the server and the server can send information to the client, simultaneously.
The Structure Chart Manager uses [receive.bucket$()](../functions_interprocess_communication_bshell/receive.bucket.md) for interprocess communication. When it sends a bucket message to the client, the client receives an event of type EVTBUCKETMESSAGE. So the client program must contain a loop to handle these events.
You can retrieve the command parameter of an event by using the following statement:
`command = evt.bms.command(event)`
The command parameter indicates the reason for the event. It can have any of the following values:
| | |
|---|---|
| MSG.PUSH.BUTTON | Indicates that the user has clicked on a button in the Structure Chart. |
| MSG.NODE.PRESS | Indicates that the user has clicked on a node of the Structure Chart. |
| MSG.NODE.DPRESS | Indicates that the user has double-clicked on a node of the Structure Chart. |
You use the following functions to retrieve data from the Structure Chart Manager after a bucket message has been received: [get.tree.node.press()](get.tree.node.press.md), [get.tree.node.dpress()](get.tree.node.dpress.md), [get.tree.push.button()](get.tree.push.button.md), [get.tree.default()](get.tree.default.md).

## Colors
All colors must be composed by using the [rgb()](../functions_color/rgb.md) function. Or you can use one of the following predefined colors:
RGB.BLACK RGB.MAGENTA RGB.RED
RGB.BLUE RGB.GREEN RGB.WHITE
RGB.YELLOW RGB.GRAY RGB.CYAN

## Related topics
- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
