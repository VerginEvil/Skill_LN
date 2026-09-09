# cmf.createAttachment()

## Syntax:
`#include <bic_cmf>`
`function long cmf.createattachment( long mid )`

## Description
Creates an attachment entry in the message identified by mid and returns the identification of the attachment.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |

## Return values
| | |
|---|---|
| <> 0 | Attachment Identification. |
| 0 | Attachment could not be created (most likely invalid cmf object). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
