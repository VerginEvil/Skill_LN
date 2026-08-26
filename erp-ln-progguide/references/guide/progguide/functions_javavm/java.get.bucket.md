# java.get.bucket

## Syntax:
`function long java.get.bucket( long Queue.id, ref string body, long length, [ ref string header ] )`

## Description
Retrieves a bucket from the queue (if available). The message is removed from the queue afterwards.

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  id of the queue to retrieve the message from  |
| `ref string` | `body` |  upon return, contains the received body  |
| `long` | `length` |  length of the data in body  |
| `[ ref string` | `header ]` |  upon return, contains the received header  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| >= 0 | upon success, return value is the number of bytes in body  |
| -1 | JavaVM not supported on this platform |
| -2 | unable to store the message into the supplied parameters  |
| -4 | no message available on queue |

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)
