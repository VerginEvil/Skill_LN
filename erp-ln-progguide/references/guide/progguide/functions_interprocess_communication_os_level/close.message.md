# close.message()

## Syntax:
`function void close.message( long key, [ long fast ] )`

## Description
This removes the specified mailbox. All messages in the mailbox are also automatically removed.

## Arguments
| | | |
|---|---|---|
| `long` | `key` |  The mailbox key, as returned by [open.message()](open.message.md).  |
| `[ long` | `fast ]` |  Set this optional argument to 1 if you are using the UNIX message queue ID instead of the mailbox key to identify the mailbox.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Interprocess communication (OS level) overview](overview.md)
- [Interprocess communication (OS level) synopsis](synopsis.md)
