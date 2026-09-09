# DsCcolorCell

## Description
A color cell is a rectangular child window that displays a color. If possible, a color cell uses only one palette entry and so saves resources. Otherwise, the number of colors used increases with every change.

## Events
A DsCcolorCell object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNbackground (long) | [CSG] | The rgb value that defines the background color of the object. If this attribute is not specified, the object inherits the background color of its parent. If none of the parent objects specify a background color, the resource workAreaBackground is used. |
| DsNborderWidth (long) | [CSG] | The width of the object's border, in pixels. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
