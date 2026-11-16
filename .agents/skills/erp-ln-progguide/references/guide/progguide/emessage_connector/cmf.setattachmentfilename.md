# cmf.setAttachmentFilename()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setattachmentfilename( long attachment, string filename, [ string displayname ] )`

## Description
Sets the physical filename of the attachment identified by *attachment* to the value *filename.* Sets the human-readable filename to *displayname*. If *displayname* is not supplied, then the readable filename is set to the physical filename.

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `string` | `filename` |  The physical filename.  |
| `[ string` | `displayname ]` |  The name of the file that is displayed. If displayname is not supplied, then the physical filename is used.  |

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
