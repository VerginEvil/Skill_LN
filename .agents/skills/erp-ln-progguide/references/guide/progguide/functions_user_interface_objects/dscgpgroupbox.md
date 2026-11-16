# DsCgpGroupBox

## Description
A DsCgpGroupBox object defines a frame on the parent window. It can also display a text string at the top of the frame. The parent object is always a DsCgwindow object.

## Events
A DsCgpGroupBox object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNgcBackground (long) | [G] | The rgb value that defines the background color of the graphical part. |
| DsNgcFontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to title text. |
| DsNgcForeground (long) | [G] | The rgb value that defines the foreground color of the graphical part. |
| DsNgc (long) | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object. |
| DsNheight (long) | [CSG] | The height of the frame, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the composite object relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject. |
| DsNstring (string) | [CSG] | The text string to be displayed at the top of the groupbox. |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNgcTextStyle (long) | [CSG] | Defines the style of the text string displayed at the top of the groupbox. Possible values are: TSNORMAL Normal text. TSBOLD Bold text. TSREVERSE Reverse text. TSUNDERLINE Underlined text. TSFILLSOLID Fill with background color. |
| DsNwidth (long) | [CSG] | The width of the frame, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the subobject's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the subobject's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
