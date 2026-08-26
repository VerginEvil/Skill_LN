# cmf.getAttachmentBody()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getattachmentbody( long attachment, enum ttyeno body )`

## Description
Gets the type of the attachment identified by *attachment* and returns it in the enum *body.*

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `enum ttyeno` | `body` |  Is attachment the bodytext: ttyeno.yes | ttyeno.no Only one attachment for each message can be the body.  |

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
