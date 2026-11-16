# DsCdrawnButton

## Description
A DsCdrawnButton object has the same functionality as a [DsCpushButton](dscpushbutton.md) object except that it displays a graphical image instead of a text label.

## Events
A DsCdrawnButton object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTBUTTONSELECT

## Attributes
| | | |
|---|---|---|
| DsNeventMask (long) | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNpixmap (long) | [CSG] | The ID of the [DsCpixmap](dscpixmap.md) object to be displayed on the button. |
| DsNreturnValue (long) | [CSG] | The value that will be returned when the button is selected. The return value must be handled as an event. See [Events overview](../events/overview.md). |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
