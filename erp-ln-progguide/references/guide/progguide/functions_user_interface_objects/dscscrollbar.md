# DsCscrollbar

## Description
Scroll bars enable users to scroll data that is too large to fit in the viewing window. They can be either horizontal or vertical. A scroll bar consists of the following components:
- A rectangular shaft (referred to as the scroll region). This represents the full amount of information available to the window.
- A scroll arrow at either end of the scroll region. Clicking on these scrolls the data by specified increments.
- A movable slider (also referred to as a scroll box). This indicates the relative position of the currently displayed data within the whole.    To scroll the data, users can click on one of the scroll arrows, click in the scroll region, or drag the slider.

## Events
A DsCscrollbar object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTSCROLLBARSELECT

## Attributes
| | | |
|---|---|---|
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNincrement (long)  | [CSG] | The amount the slider value changes when the user moves the slider by one increment. Clicking on one of the scroll arrows moves the slider one increment towards the arrow. If a negative value is specified, the absolute value is used.  |
|  DsNmaximum (long)  | [CSG] | The maximum value of the slider. This corresponds to the right or bottom position of the slider.  |
|  DsNminimum (long)  | [CSG] | The minimum value of the slider. This corresponds to the left or top position of the slider. DsNmaximum can be less than DsNminimum.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNorientation (long)  | [CSG] |  The orientation of the scroll bar. Possible values are: DSHORIZONTAL DSVERTICAL (default)  |
| DsNpageIncrement | [CSG] | The amount the slider value changes when the user moves the slider by one page increment. Clicking in the scroll region moves the slider one page increment in the direction of the click. If a negative value is specified, the absolute value is used.  |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNsize (long)  | [CSG] | The size of the scroll bar control, in pixels. This specifies the width of horizontal scroll bars and the height of vertical scroll bars. The default value is 100.  |
|  DsNsliderValue (long)  | [CSG] | The value corresponding to one side of the slider.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
