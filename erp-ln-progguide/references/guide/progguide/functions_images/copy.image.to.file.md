# copy.image.to.file()

## Syntax:
`function long copy.image.to.file( long source.company, string source.guid, string source.tablename, string target.file )`

## Description
This function will copy an image based on its company, guid, and table into a file.

## Arguments
| | | |
|---|---|---|
| `long` | `source.company` |  The company for which the existing image is stored.  |
| `string` | `source.guid` |  The unique identification of an image existing in the repository.  |
| `string` | `source.tablename` |  The name of the table to which the source image is linked.  |
| `string` | `target.file` |  The file to which the image is copied.  |

## Return values
| | |
|---|---|
| 0 | Successful |
| -2 | The source Image does not exist |
| -3 | Company switch failed |
| -4 | Failed to call the copy function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2360.

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms synopsis](synopsis.md)
- [Images on Forms Examples](examples.md)
