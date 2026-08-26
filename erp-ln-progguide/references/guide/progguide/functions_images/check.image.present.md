# check.image.present()

## Syntax:
`function boolean check.image.present( string guid, [ string tablename, long width, long height ] )`

## Description
This function will check whether an image set is already present in the repository.

## Arguments
| | | |
|---|---|---|
| `string` | `guid` |  The unique identification that is assigned to this image set  |
| `[ string` | `tablename ]` |  Optional argument in which the name of the table to which this image is linked is passed. The default value is the current maintable.  |
| `[ long` | `width ]` |  Optional argument for the width of the image.  |
| `[ long` | `height ]` |  Optional argument for the height of the image.  |

## Return values
| | |
|---|---|
| true | When this image set is present in the repository |
| false | otherwise |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)
- [Images on Forms synopsis](synopsis.md)
- [Images on Forms Examples](examples.md)
