# get.image.path()

## Syntax:
`function string get.image.path( string guid, long sequ, [ string tablename, long width, long height ] )`

## Description
This function will get the full path for an image.

## Arguments
| | | |
|---|---|---|
| `string` | `guid` |  The unique identification that is assigned to this image set  |
| `long` | `sequ` |  The one based image sequence number within the image set  |
| `[ string` | `tablename ]` |  Optional argument in which the name of the table to which this image is linked is passed. The default value is the current maintable.  |
| `[ long` | `width ]` |  Optional argument for the width of the image.  |
| `[ long` | `height ]` |  Optional argument for the height of the image.  |

## Return values
The path for the requested image, empty string if the requested image cannot be found.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
