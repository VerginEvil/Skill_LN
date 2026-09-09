# create.tree.button()

## Syntax:
`function void create.tree.button( string tree_name, long button_id, string button_desc, [ long process_id ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This adds a button to a specified tree. The client program can link a session or command to this button. An event is sent to the client when the user clicks on the button.

## Arguments
| | | |
|---|---|---|
| `string` | `tree_name` |  The name of the tree to which the button must be added.  |
| `long` | `button_id` |  The unique ID of the new button.  |
| `string` | `button_desc` |  The text for the button's label.  |
| `[ long` | `process_id ]` |  This optional argument indicates the process ID of the server to which the button must be added, as returned by [create.tree()](create.tree.md). If you do not include this argument, the button is added to all servers with the name specified in *tree_name*.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
