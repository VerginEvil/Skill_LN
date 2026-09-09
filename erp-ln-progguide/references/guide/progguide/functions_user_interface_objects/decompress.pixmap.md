# decompress.pixmap()

## Syntax:
`function long decompress.pixmap( string buffer, ref long colormap, ref string pixmap )`

## Description
This converts a picture in.gif format to a colormap and pixmap. The long array returned by the *colormap* argument can subsequently be used as the DsNcolorTable attribute of a DsCcolormap object. The string array returned by the *pixmap* argument can subsequently be used as the DsNdata attribute for a DsCpixmap object.

## Arguments
| | | |
|---|---|---|
| `string` | `buffer` |  The buffer containing the.gif file data, as returned by a [seq.read()](../functions_directory_file_operations/seq.read.md) call.  |
| `ref long` | `colormap` |  This returns an array of rgb values that you can use as the DsNcolorTable attribute for DsCcolormap objects.  |
| `ref string` | `pixmap` |  This returns an array of indexes into the returned colormap. You can use this as the DsNdata attribute of DsCpixmap objects.  |

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
