# cmf.getAttachmentPosition()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getattachmentposition( long attachment, string position(10) )`

## Description
Gets the position of the attachment identified by *attachment* and returns it in the string *position.*

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `string` | `position(10)` |  The attachment position determines the number of characters (of the bodytext) after which the attachment-icon will be placed.  |

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
