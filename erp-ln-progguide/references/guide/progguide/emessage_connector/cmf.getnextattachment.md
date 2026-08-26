# cmf.getNextAttachment()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getnextattachment( long mid, long previous )`

## Description
Gets an attachment entry in the message identified by mid and returns the identification of the attachment. If *previous* is 0 (no valid object id), then the first attachment is returned. If *previous* is a valid object id (not 0) then the attachment id of the attachment that follows the attachment identified by *previous* is returned. Subsequent calls to this function return succeeding attachments. The current attachment pointer can be reset by setting *previous* to 0 again.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `long` | `previous` |  The identification of the attachment. If *previous* is 0 (no valid object id), then the first attachment is returned. If *previous* is a valid object id (not 0) then the attachment id of the attachment that follows the attachment identified by *previous* is returned.  |

## Return values
| | |
|---|---|
| <> 0 | Attachment Identification. |
| 0 | Attachment could not be found (most likely end of attachment list).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
