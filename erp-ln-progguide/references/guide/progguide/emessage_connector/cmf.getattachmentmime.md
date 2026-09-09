# cmf.getAttachmentMime()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getattachmentmime( long attachment, ref string mime )`

## Description
Gets the mime type of the attachment identified by *attachment* and returns it in the string *mime.*

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `ref string` | `mime` |    |

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
