# cmf.getAttachmentFilename()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getattachmentfilename( long attachment, string filename, ref string displayname )`

## Description
Gets the filename and display name of the attachment identified by *attachment* and returns them in the strings *filename* and *displayname.*

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `string` | `filename` |  The physical filename.  |
| `ref string` | `displayname` |  The name of the file that is displayed. If displayname is not supplied, then the physical filename is used.  |

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
