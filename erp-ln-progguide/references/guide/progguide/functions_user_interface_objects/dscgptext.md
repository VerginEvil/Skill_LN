# DsCgpText

## Description
A DsCgpText subobject defines a text string to be drawn as a graphical part in the parent window. The parent window is always a DsCgwindow object.

## Events
A DsCgpText subobject does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNgcBackground (long) | [CSG] | The rgb value that defines the background color of the graphical part. |
| DsNgcFontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the text. |
| DsNgcForeground (long) | [CSG] | The rgb value that defines the foreground color of the graphical part. |
| DsNgc (long) | [CS] | The ID of a [DsCgc](dscgc.md) object that contains a set of attributes to be applied to the object. |
| DsNheight (long) | [G] | The height of the text string, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the text object relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn below DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject. |
| DsNstring (string) | [CSG] | The text string to display as graphical text. |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNgcTextStyle (long) | [CSG] | Defines the style of the graphical text. Possible values are: TSNORMAL Normal text. TSBOLD Bold text. TSREVERSE Reverse text. TSUNDERLINE Underlined text. TSFILLSOLID Fill with background color. |
| DsNwidth (long) | [G] | The width of the text string, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the baseline starting position for the string, in pixels, relative to the upper-left corner of the parent window. |
| DsNy (long) | [CSG] | The y-coordinate of the baseline starting position for the string, in pixels, relative to the upper-left corner of the parent window. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
