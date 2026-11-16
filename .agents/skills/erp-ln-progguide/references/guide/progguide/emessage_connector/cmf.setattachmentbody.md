# cmf.setAttachmentBody()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setattachmentbody( long attachment, enum body )`

## Description
Sets the type of the attachment identified by *attachment* to the value *body.* If body is “YES”, then the attachment is considered to be the bodytext. Only one body attachment is allowed for each message object, although this is NOT enforced by the Infor LN eMessage Connector.

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `enum` | `body` |  Is attachment the bodytext: ttyeno.yes | ttyeno.no Only one attachment for each message can be the body.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid attachment identification. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
