# DsCtabFrame

## Description
A DsCtabFrame object provides a window with one or more form tabs. The tabs can be arranged in a single line or in multiple lines. When tabs are arranged on a single line, scroll buttons are added automatically if the window is not large enough to accommodate all the tabs.
A tab frame object can have multiple children. Children are automatically positioned at the top-left of the tab frame. The size of the tab frame window automatically adjusts to accommodate the largest child.

## Events
A DsCtabFrame object can generate the following events:
EVTTABSELECT
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS

## Attributes
| | | |
|---|---|---|
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfixedWidth (boolean)  | [CG] | Specifies whether or not all tabs have the same width. The default is FALSE. |
|  DsNfontSet (long)  | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to tab titles. The default font is the Windows default font.  |
|  DsNheight (long)  | [CSG] | The height (in pixels) of the client area of the tab frame window. If this is not specified, the height of the tab frame adjusts to accommodate the largest child window.  |
|  DsNmultiLine (boolean)  | [CG] | Specifies whether or not the tabs are arranged on multiple lines. The default is FALSE.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNselected (long)  | [CSG] | Use to select a particular tab by tab number. The tab numbers range from 1 to the total number of tabs. The default is 1. |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstring (string)  | [CSG] | The text of the tab titles. Separate the text for each tab by \n. The number of title strings entered determines the number of form tabs displayed. This attribute is mandatory when creating a tab frame.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width (in pixels) of the client area of the tab frame window. If this is not specified, the width of the tab frame adjusts to accommodate the largest child window.  |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
