# DsCgpImage

## Description
A DsCgpImage object defines a graphical image to be drawn in the parent window. It is linked to a DsCpixmap object, which defines an array of pixels, with a specified width, height, and depth (number of planes), but no screen coordinates. The parent window is always a DsCgwindow object.

## Events
A DsCgpImage subobject does not generate events.

## Attributes
| | | |
|---|---|---|
|  DsNattribute (long)  | [CSG] |  The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden.  |
|  DsNheight (long)  | [G] | The height of the image, in pixels. |
|  DsNobjectType (long)  | [G] | The subobject type. |
|  DsNpixmap (long)  | [CS] | The ID of the pixmap to be drawn. |
|  DsNrefSubObject (long)  | [CS] | The ID of the subobject used as a reference by DsNsequence.  |
|  DsNsequence (long)  | [CS] |  The position of the image relative to the reference subobject. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject.  |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
| DsNwidth | [G] | The width of the image, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the subobject's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the subobject's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
