# java.lookup.queue

## Syntax:
`function long java.lookup.queue( long Queue.id, [ ref string header ] )`

## Description
Checks whether a queue is still valid and, if so, if the queue contains a message. The message is not removed from the queue.

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  id of the queue to verify.  |
| `[ ref string` | `header ]` |  contains the header of the first message on the queue.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| >= 0 | upon success, return value is the number of bytes in body  |
| -1 | JavaVM not supported on this platform or |
| -1 | incorrect queue ID |
| -4 | no message available on queue |

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
