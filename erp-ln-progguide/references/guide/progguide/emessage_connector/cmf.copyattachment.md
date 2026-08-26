# cmf.copyAttachment()

## Syntax:
`#include <bic_cmf>`
`function long cmf.copyattachment( long attachment.id, long oid )`

## Description
Copies the attachment identified by attachment.id from the object identified by id1 to the object identified by id2. All attributes and their values are also copied

## Arguments
| | | |
|---|---|---|
| `long` | `attachment.id` |  Identification of the source attachment.  |
| `long` | `oid` |  Identification of the destination attachment.  |

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
