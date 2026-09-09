# save.image.file()

## Syntax:
`function boolean save.image.file( string guid, long sequence, string pathname, [ string tablename ] )`

## Description
This function will save an image file into the image repository (put it at proper place in directory and update the image table). This function can be used by an image import application.

## Arguments
| | | |
|---|---|---|
| `string` | `guid` |  The unique identification that will be assigned to this image set.  |
| `long` | `sequence` |  A one based sequence number to identify a specific image in the set.  |
| `string` | `pathname` |  The absolute pathname of the image file to be saved in the repository  |
| `[ string` | `tablename ]` |  Optional argument in which the name of the table to which this image is linked is passed. The default value is the current maintable.  |

## Return values
| | |
|---|---|
| true | When successful |
| false | When an error occurred |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Images on Forms Overview](overview.md)

- [Images on Forms synopsis](synopsis.md)

- [Images on Forms Examples](examples.md)
