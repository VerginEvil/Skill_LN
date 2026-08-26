# java.destroy.queue

## Syntax:
`function long java.destroy.queue( long Queue.id )`

## Description
Removes a queue, given the queue id. This will also remove all buckets on that queue!!

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  id of the queue to be removed  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | upon success |
| -1 | JavaVM not supported on this platform |
| -4 | incorrect queue ID |
| -5 | unable to remove the queue |

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
