# DsCcheckBox

## Description
A check box represents a choice that has two states (selected or not selected). It appears as a square box with an accompanying label. When the choice is selected, a check mark appears in the box. When the choice is not selected, the box is empty.
Users can toggle a check box on and off with the mouse or keyboard keys. Check boxes are typically used in a group to provide a multiple-choice field. Within a group, they represent independent choices that are not mutually exclusive.

## Events
A DsCcheckBox object can generate the following event types:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTBUTTONSELECT

## Attributes
| | | |
|---|---|---|
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfontSet (long)  | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the label text. If this attribute is not set, the Windows default font is used.  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNjustify (long)  | [CSG] |  The alignment of the label text. Possible values are: DSJUSTIFYLEFT (default) DSJUSTIFYRIGHT DSJUSTIFYCENTER  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNset (long)  | [CSG] |  The state of the check box. Possible values are: TRUE Check box selected. FALSE Check box not selected (default).  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstring (string)  | [CSG] | The label text. |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
