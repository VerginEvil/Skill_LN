# DsCpixmap

## Description
A DsCpixmap object defines a graphical image. It consists of a two-dimensional array of pixels, with a specified width, height, and depth (number of planes), but no screen coordinates. A pixmap is a resource that is used by other objects that can display an image. Objects that can use a pixmap include DsCdrawnButton, DsCgpImage and DsCtoolBar objects.

## Events
A DsCpixmap object does not generate events.

## Attributes
| | | |
|---|---|---|
|  DsNbackgroundMode (long)  | [CS] |  Specifies the pixmap's background mode. Possible values are: DSTRANSPARENT DSOPAQUE (default)  |
|  DsNcolormap (long)  | [CS] | The object ID of a DsCcolormap object. The color map defines an array of colors that the pixmap uses when DsNdataType is set to DSPIXMAP8.  |
|  DsNdata (long array)  | [CS] | An array of indexes into the contents of a .gif file or into the color table of the DsCcolormap object specified by DsNcolormap.  |
|  DsNdataType (long)  | [CS] |  The pixmap type. Possible values are: DSPIXMAP8 DSPIXGIF8  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
