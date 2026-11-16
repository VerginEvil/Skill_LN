# get.tree.push.button()

## Syntax:
`function void get.tree.push.button( ref long event, ref long process_id, ref string button_id, ref string node_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use this function to retrieve data from the Structure Chart Manager after an EVTBUCKETMESSAGE-type event, with a MSG.PUSH.BUTTON command, has been received.

## Arguments
| | | |
|---|---|---|
| `ref long` | `event` |  The event containing the MSG.PUSH.BUTTON command.  |
| `ref long` | `process_id` |  This returns the process ID of the Structure Chart Manager that sent the message.  |
| `ref string` | `button_id` |    |
| `ref string` | `node_id` |  This returns the ID of the relevant node.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Structure Chart Manager overview](overview.md)

- [Structure ChartManager synopsis](synopsis.md)

- [Tree structures: example](example.md)
