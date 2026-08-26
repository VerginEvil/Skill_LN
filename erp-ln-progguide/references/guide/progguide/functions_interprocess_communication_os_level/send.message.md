# send.message()

## Syntax:
`function long send.message( long dest.key, long sender.key, string message$, long fast )`

## Description
This stores a message in the specified mailbox. The process must previously have connected to the mailbox by calling [open.message()](open.message.md).

## Arguments
| | | |
|---|---|---|
| `long` | `dest.key` |  The mailbox key, as returned by [open.message()](open.message.md).  |
| `long` | `sender.key` |  This is a unique key that identifies the sender of the message. Processes reading from the mailbox can use this filter out messages from other senders.  |
| `string` | `message$` |  This is the message to be sent to the mailbox.  |
| `long` | `fast` |  Set this optional argument to 1 if you are using the UNIX message queue ID instead of the mailbox key to identify the mailbox.  |

## Return values
This returns 0 when successful. Otherwise it returns an error number.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
- [Interprocess communication (OS level) synopsis](synopsis.md)
