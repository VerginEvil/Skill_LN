# DsCgpHeader

## Description
A DsCgpHeader subobject defines a header line on the parent window. The line can include a centered title string. The parent window is always a DsCgwindow object.

## Events
A DsCgpHeader object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNgcBackground (long) | [G] | The rgb value that defines the background color of the graphical part. |
| DsNgcFontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to subobject's text string. |
| DsNgcForeground (long) | [G] | The rgb value that defines the foreground color of the graphical part. |
| DsNgc (long) | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object. |
| DsNheight (long) | [G] | The height of the header line, in pixels. |
| DsNobjectType (long) | [G] | The subobject type. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the header subobject relative to the reference subobject. Possible values are: GPMKFIRST part is drawn above all other parts GPMKLAST part is drawn under all other parts GPMKNEXT part is drawn under DsNrefSubObject GPMKPREV part is drawn above DsNrefSubObject |
| DsNstring (string) | [CSG] | The text string to be displayed in the center of the header line. |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNgcTextStyle (long) | [CSG] | Defines the style of the text string displayed in the center of the header line. Possible values are: TSNORMAL normal text TSBOLD bold text TSREVERSE reverse text TSUNDERLINE underlined text TSFILLSOLID fill with background color |
| DsNwidth (long) | [CSG] | The width of the header line, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the subobject's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the subobject's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
