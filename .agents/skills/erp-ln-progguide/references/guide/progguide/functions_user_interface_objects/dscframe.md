# DsCframe

## Description
A DsCframe object places a three-dimensional border around a single child object.

## Events
A DsCframe object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNfontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the title string defined by DsNstring. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNshadowType (long) | [CG] | The frame's border style. Possible values are: DSSHADOWNONE No shadowed border. DSSHADOWIN Frame appears inset. DSSHADOWOUT Frame appears outset (default). DSSHADOWETCHEDIN Frame uses the grouping border style. DSSHADOWGROUPBOX Frame uses the grouping border style – this frame style can display a title string (left aligned). |
| DsNstring (string) | [CSG] | The text string for the frame title. This is visible only when DsNshadowType is DSSHADOWGROUPBOX. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
