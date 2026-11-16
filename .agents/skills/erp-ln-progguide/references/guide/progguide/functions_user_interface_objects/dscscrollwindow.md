# DsCscrollWindow

## Description
A DsCscrollWindow object provides a scrollable view of a child object. It supports a single child object only. Scroll bars enable users to view the data not currently visible in the window. Scroll bars are visible only when the child object is larger than the scroll window.

## Events
A DsCscrollWindow object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNchildPosX (long) | [CSG] | The distance (in pixels) from the left edge of the child object to the left edge of the scroll window. |
| DsNchildPosY (long) | [CSG] | The distance (in pixels) from the top edge of the child object to the top edge of the scroll window. |
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
