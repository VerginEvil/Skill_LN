# compress.pixmap()

## Syntax:
`function long compress.pixmap( long colormap, long num_colors, string pixmap(), long width, long height, ref string buffer, ref long buffer_length )`

## Description
This converts a specified colormap and pixmap to a picture in.gif format.

## Arguments
| | | |
|---|---|---|
| `long` | `colormap` |  The ID of the DsCcolormap object that must be converted.  |
| `long` | `num_colors` |  The number of colors defined by the specified colormap object.  |
| `string` | `pixmap()` |  The ID of the DsCpixmap object that must be converted.  |
| `long` | `width` |  The width of the pixmap, in pixels.  |
| `long` | `height` |  The height of the pixmap, in pixels.  |
| `ref string` | `buffer` |  This returns the data for the.gif picture. To access the.gif picture, you must write the buffer data to a file by calling [seq.write()](../functions_directory_file_operations/seq.write.md).  |
| `ref long` | `buffer_length` |  This returns the length of the buffer.  |

## Return values
TRUE (<> 0): success
FALSE (0): error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
