# cmf.getMessageId()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getmessageid( long mid, ref string messageId )`

## Description
Gets the message id of the message identified by *mid* and return string into *messageId.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref string` | `messageId` |  Unique identification of a message within Infor LN eMessage Connector.  |

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
