# copy.image()

## Syntax:
`function long copy.image( string source.guid, string source.tablename, string target.guid, string target.tablename, [ boolean overwrite ] )`

## Description
This function will copy an image or set of images based on its guid into then image repository refered by the target guid. This function can be used when copying records.

## Arguments
| | | |
|---|---|---|
| `string` | `source.guid` |  The unique identification of an image existing in the repository.  |
| `string` | `source.tablename` |  The name of that table to which the source image is linked.  |
| `string` | `target.guid` |  The unique identification for the copy of the image.  |
| `string` | `target.tablename` |  The name of that table to which the target image should be linked.  |
| `[ boolean` | `overwrite ]` |  If for the target guid/table already an image or set of images exist then these will be deleted and overwritten with the image (set) referred by the source.guid. Default value for overwrite is true.  |

## Return values
| | |
|---|---|
| 0 | Successful |
| -1 | The target exist and overwrite was false |
| -2 | The source Image does not exist |
| -3 | The copy of the image failed |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
