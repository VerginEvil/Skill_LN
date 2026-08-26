# recv.message()

## Syntax:
`function long recv.message( long key, long sender.key, long time, ref string message$, [ long fast ] )`

## Description
This reads a message from the specified mailbox. The process must previously have connected to the mailbox by calling [open.message()](open.message.md).

## Arguments
| | | |
|---|---|---|
| `long` | `key` |  The mailbox key, as returned by [open.message()](open.message.md).  |
| `long` | `sender.key` |  Messages sent with the [send.message()](send.message.md) function have an associated sender key which identifies the sender. To retrieve the next message from a particular sender, specify that sender's key here. Otherwise specify zero – in this case the function retrieves the next message in the mailbox, regardless of the sender.  |
| `long` | `time` |  Use this to specify the maximum time that the function must wait before returning. If you set this to -1, the function waits until a message arrives in the mailbox.  |
| `ref string` | `message$` |  This stores the retrieved message.  |
| `[ long` | `fast ]` |  Set this optional argument to 1 if you are using the UNIX message queue ID instead of the mailbox key to identify the mailbox.  |

## Return values
This returns the sender key. It returns -1 if an error occurs (the predefined variable *e* contains the error number).

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
- [Interprocess communication (OS level) synopsis](synopsis.md)
