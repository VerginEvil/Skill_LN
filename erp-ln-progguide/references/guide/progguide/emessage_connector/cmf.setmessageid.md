# cmf.setMessageId()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setmessageid( long mid, string messageId )`

## Description
Sets the message ID of the message identified by *mid* and returns string into *messageId.* The messageId is a string that uniquely identifies a message within Infor LN eMessage Connector. The application using Baan eMessage Connector need not to call this function as Infor LN eMessage Connector will take care of this automatically.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `string` | `messageId` |  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id or element not present).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
