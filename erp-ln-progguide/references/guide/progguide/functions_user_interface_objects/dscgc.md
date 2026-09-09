# DsCgc

## Description
A graphical context object (DsCgc) defines a set of attributes that can be applied to graphical parts (that is, to subobjects of type DsCgpArc, DsCgpLine, DsCgpPie, and so on).
When multiple graphical parts have common attributes, you can define those attributes in a DsCgc object instead of specifying them individually for each graphical part. You can then apply the attributes to a graphical part by specifying the ID of the relevant DsCgc object in the DsNgc attribute of the graphical part. Using this mechanism improves performance because less data needs to be transferred between the bshell and the user interface.

## Events
A DsCgc object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNgcBackground (long) | [CSG] | The rgb value that defines the background color of the graphical part. |
| DsNgcCapStyle (long) | [CSG] | This controls the appearance of line ends. Possible values are: GCCAPBUTT Lines are square at the endpoint. GCCAPROUND Lines are terminated by a circular arc whose diameter equals the line width. |
| DsNgcFillColor (long) | [CSG] | The rgb value that defines the fill color of the graphical part. This is relevant only to polygons, rectangles, and pies. |
| DsNgcFillStyle (long) | [CSG] | The fill style for a graphical part. Possible values are: GCFILLSOLID Fill solid. GCFILL90 Fill 90 %. GCFILL75 Fill 75 %. GCFILL50 Fill 50 %. GCFILL25 Fill 25 %. GCFILL10 Fill 10 %. GCFILL00 Fill 0 %. GCFILLHOR Fill with horizontal lines. GCFILLVER Fill with vertical lines. GCFILLSLEFT Fill with slant left lines. GCFILLSRIGHT Fill with slant right lines. GCFILLHOLLOW Do not fill. |
| DsNgcFontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to text in the graphical part. |
| DsNgcForeground (long) | [CSG] | The rgb value that defines the foreground color of the graphical part. |
| DsNgcJoinStyle (long) | [CSG] | Defines how corners are drawn. Possible values are: GCJOINMITER The outer edges of the two lines extend to meet at an angle. GCJOINROUND Lines are joined by a circular arc whose diameter equals the line width and which is centered on the join point. |
| DsNgcLineStyle (long) | [CSG] | The line and border style for a graphical part. Possible values are: GCLINESOLID Normal line. GCLINEDOUBLEDASH Line stippled, using DsNgcForeground and DsNgcBackground colors. GCLINEONOFFDASH Line stippled, using DsNgcForeground and the window's background color. |
| DsNgcLineWidth (long) | [CSG] | The width of lines and borders, in pixels. |
| DsNgcTextStyle (long) | [CSG] | Defines the style of graphical text. Possible values are: TSNORMAL Normal text TSBOLD Bold text TSREVERSE Reverse text TSUNDERLINE Underlined text TSFILLSOLID Fill with background color |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNtemplate | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
