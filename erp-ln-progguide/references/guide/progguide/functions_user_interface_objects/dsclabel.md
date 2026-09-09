# DsClabel

## Description
A DsClabel object provides a text string for labeling other objects.

## Events
A DsClabel object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNfontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to label text The default font is the Windows default font. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNjustify (long) | [CSG] | The alignment of the text string within the label object. Possible values are: DSJUSTIFYLEFT (default) DSJUSTIFYRIGHT DSJUSTIFYCENTER |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNstring (string) | [CSG] | The label string. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
