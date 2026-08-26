# DsCpushButton

## Description
A pushbutton, also referred to as a command button, represents an action that is carried out when the user selects the button. A pushbutton displays a text label.
A [DsCdrawnButton](dscdrawnbutton.md) object has the same functionality as a DsCpushButton object except that it displays a graphical image instead of a text label.

## Events
A DsCpushButton object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTBUTTONSELECT

## Attributes
| | | |
|---|---|---|
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfontSet (long)  | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the label on the pushbutton The default font is the Windows default font.  |
|  DsNheight (long)  | [CSG] | The height of the object, in pixels. |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNreturnValue (long)  | [CSG] | The value that is returned when the pushbutton is selected. The return value must be handled as an event. See [Events overview](../events/overview.md).  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNshowAsDefault (long)  | [CSG] | Indicates whether of not the button is the default button. If TRUE, the button has a thicker border and can be activated with the ENTER key.  |
|  DsNstring (string)  | [CSG] | The text string for the button's label. |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
