# DsCslider

## Description
A slider object is used to set a value in a continuous range of values (for example, volume or brightness). It consists of a scroll bar that represents the full range of values and a movable slider whose position represents the current value. It also includes labels that indicate the slider's current, maximum, and minimum values. Tick marks are optional.

## Events
A DsCslider object can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTSCROLLBARSELECT

## Attributes
| | | |
|---|---|---|
| DsNeventMask (long) | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks. |
| DsNfontSet (long) | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the slider's labels. The default font is the Windows default font. |
| DsNincrement (long) | [CSG] | The amount the slider value changes when the user moves the slider by one increment. |
| DsNmaximum (long) | [CSG] | The maximum value of the slider. This corresponds to the right or bottom position of the slider. |
| DsNminimum (long) | [CSG] | The minimum value of the slider. This corresponds to the left or top position of the slider. DsNmaximum can be less than DsNminimum. |
| DsNobjectType (long) | [G] | The object type. |
| DsNorientation (long) | [CSG] | The orientation of the slider object. Possible values are: DSHORIZONTAL DSVERTICAL (default) |
| DsNpageIncrement | [CSG] | The amount the slider value changes when the user moves the slider by one page increment. Clicking in the slider bar moves the slider one page increment in the direction of the click. If a negative value is specified, the absolute value is used. |
| DsNparent (long) | [G] | The ID of the parent object. |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |
| DsNsize (long) | [CSG] | The size of the slider in pixels. For horizontal sliders, it specifies the width of the slider. For vertical sliders, it specifies the height. The default value is 100. |
| DsNsliderValue (long) | [CSG] | The value corresponding to one side of the slider. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |
| DsNtickFrequency (long) | [CSG] | The frequency of tick marks on the slider. This can be any interval from 0 to DsNmaximum - DsNminimum. The default is 0. DsNtickStyle must not be DSNTICKNONE. |
| DsNtickStyle (long) | [CSG] | The positioning of tick marks on the slider. Possible values are: DSTICKNONE No tick marks. DSTICKTOP Tick marks above slider (DSHORIZONTAL). DSTICKBOTTOM Tick marks below slider (DSHORIZONTAL). DSTICKRIGHT Tick marks to right of slider (DSVERTICAL). DSTICKLEFT Tick marks to left of slider (DSVERTICAL). DSTICKBOTH Tick marks on both sides of slider (default). |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
