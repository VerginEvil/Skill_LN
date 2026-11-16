# DsCgpRectangle

## Description
A DsCgpRectangle subobject defines a rectangle within the parent window. The parent window is always a DsCgwindow object.

## Events
A DsCgpRectangle subobject does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNgcBackground (long) | [CSG] | The rgb value that defines the background color of the subobject. |
| DsNgcFillColor (long) | [CSG] | The rgb value that defines the fill color of the graphical part. |
| DsNgcFillStyle (long) | [CSG] | The fill style for a graphical part. Possible values are: GCFILLSOLID Fill solid. GCFILL90 Fill 90 %. GCFILL75 Fill 75 %. GCFILL50 Fill 50 %. GCFILL25 Fill 25 %. GCFILL10 Fill 10 %. GCFILL00 Fill 0 %. GCFILLHOR Fill with horizontal lines. GCFILLVER Fill with vertical lines. GCFILLSLEFT Fill with slant left lines. GCFILLSRIGHT Fill with slant right lines GCFILLHOLLOW Do not fill. |
| DsNgcForeground (long) | [CSG] | The rgb value that defines the foreground color of the graphical part. |
| DsNgc (long) | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object. |
| DsNgcJoinStyle (long) | [CSG] | Defines how corners are drawn. Possible values are: GCJOINMITER The outer edges of the two lines extend to meet at an angle. GCJOINROUND Lines are joined by a circular arc whose diameter equals the line width and which is centered on the join point. |
| DsNgcLineStyle (long) | [CSG] | The line and border style for a graphical part. Possible values are: GCLINESOLID Normal line. GCLINEDOUBLEDASH Line stippled, using DsNgcForeground and DsNgcBackground colors. GCLINEONOFFDASH Line stippled, using DsNgcForeground and the window's background color. |
| DsNgcLineWidth (long) | [CSG] | The width of lines and borders, in pixels. |
| DsNheight (long) | [CSG] | The height of the rectangle, in pixels. |
| DsNobjectType (long) | [G] | The subobject type. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the subobject relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject. |
| DsNwidth (long) | [CSG] | The width of the rectangle, in pixels. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNx (long) | [CSG] | The x-coordinate of the upper-left corner of the rectangle, in pixels, relative to the upper-left corner of the parent window. |
| DsNy (long) | [CSG] | The y-coordinate of the upper-left corner of the rectangle, in pixels, relative to the upper-left corner of the parent window. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
