# get.pixmap.info()

## Syntax:
`function long get.pixmap.info( ref string buffer, ref long num_colors, ref long width, ref long height )`

## Description
This retrieves information about a picture, in.gif format, that has been read with the [seq.read()](../functions_directory_file_operations/seq.read.md) function. It returns the number of colors in the picture and the picture's width and height. When a picture is used in an object, the width and height values are necessary for determining the amount of memory that must be allocated for the picture.

## Arguments
| | | |
|---|---|---|
| `ref string` | `buffer` |  The buffer containing the data retrieved by *seq.read()*.  |
| `ref long` | `num_colors` |  This returns the number of colors used in the picture.  |
| `ref long` | `width` |  This returns the width of the picture, in pixels.  |
| `ref long` | `height` |  This returns the height of the picture, in pixels.  |

## Return values
TRUE success
FALSE error

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
