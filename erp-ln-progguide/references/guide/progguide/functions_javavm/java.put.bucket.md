# java.put.bucket

## Syntax:
`function long java.put.bucket( long Queue.id, string body, long length, [ string header ] )`

## Description
Places a message onto a queue. The message contains a header (of type string) and a body (which can contain any character).

## Arguments
| | | |
|---|---|---|
| `long` | `Queue.id` |  Id of the queue to write the message to.  |
| `string` | `body` |  Data to be placed into the body of the message.  |
| `long` | `length` |  Length of the data in body.  |
| `[ string` | `header ]` |  A string containing the header of the message (optional).  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return codes
| | |
|---|---|
| 0 | Success. |
| -1 | JavaVM not supported on this platform. |
| -4 | Incorrect queue ID. |
| -5 | Unable to retrieve the message out of the supplied parameters. |
| -6 | Unable to place the message onto the queue. |

## Related topics
- [Java VM integration - Infor Enterprise Server 3GL](overview.md)

- [java.get.bucket](java.get.bucket.md)
