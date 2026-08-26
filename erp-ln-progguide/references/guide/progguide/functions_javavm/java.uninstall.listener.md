# java.uninstall.listener

## Syntax:
`function long java.uninstall.listener( long Queue.id )`

## Description
Uninstalls a listener at the Infor Enterprise Server side. All buckets on this queue will remain available. The listener can only be uninstalled by the process that installed the listener.

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  id of the queue from which to remove the listener  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | upon success |
| -1 | JavaVM not supported on this platform |
| -4 | incorrect queue ID |
| -5 | unable to remove the listener on the queue |

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
