# publish.message()

## Syntax:
`function long publish.message( long publication.id, long message.xml, ref long result.xml )`

## Description
This function publishes the specified message.

## Arguments
| | | |
|---|---|---|
| `long` | `publication.id` |  (input) id for publication channel, which is provided as the return value of [publish.open()](publish.open.md)  |
| `long` | `message.xml` |  (input) message to be published, which is an xml structure.  |
| `ref long` | `result.xml` |  (output): xml containing result in case of errors or warnings; see [Outbound Publishing functions overview](overview.md) for details.  |

## Return values
| | |
|---|---|
| 0 | success. |
| <> 0 | an error value |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  A successful execution of this function need not imply that the message has arrived at all applications that subscribed to the message. Depending on how the OpenWorld Adapter is configured, delivery may be asynchronous. In that case the return value only indicates that the message was posted successfully. Additionally, if the Adapter does the error handling itself, no error value or result is returned.

## Related topics
- [Outbound Publishing functions overview](overview.md)
- [Outbound Publishing functions synopsis](synopsis.md)
