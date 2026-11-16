# DsCradioButton

## Description
A radio button (also referred to as an option button) represents a single option within a set of mutually exclusive options. It is either set or not set. Within a group of radio buttons, only one option in the group can be set. Selecting one radio button automatically deselects all others in the group. A partially filled in circle indicates the currently selected button. All radio buttons have an associated label.

## Events
A DsCradioButton object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTBUTTONSELECT

## Attributes
| | | |
|---|---|---|
| DsNeventMask (long) | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks. |
| DsNfontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the radio button's label. The default font is the Windows default font. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |
| DsNjustify (long) | [CSG] | The alignment of the text string within the radio button window. Possible values are: DSJUSTIFYLEFT (default) DSJUSTIFYRIGHT DSJUSTIFYCENTER |
| DsNobjectType (long) | [G] | The object type. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNset (long) | [CSG] | The state of the button (selected or unselected). The default is FALSE. |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNstring (string) | [CSG] | The string value for the radio button's label. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
