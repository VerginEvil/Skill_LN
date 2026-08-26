# cmf.setAttachmentMIME()

## Syntax:
`function long cmf.setattachmentmime( long attachment, string mimetype )`

## Description
Sets the mime type of the attachment identified by *attachment* to the value *mime.*

## Arguments
| | | |
|---|---|---|
| `long` | `attachment` |  The attachment identification.  |
| `string` | `mimetype` |  |

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
