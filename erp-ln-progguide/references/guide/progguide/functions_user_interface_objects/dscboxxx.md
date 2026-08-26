# DsCcomBox, DsCdDComBox, DsClistBox, DsCdDListBox

## Description
A *list box* (DsClistBox) displays a list of choices from which the user can select one or more items.
A *drop-down list* *box* (DsCdDListBox) also displays a list of choices, but the list is displayed only on demand and the user can select only a single item. Users must open the control to view the list. When the list is closed, the control displays the current value.
A *combo box* (DsCcomBox) is a combination of a text box and a single-selection list box. Users can type their choice in the text box or select an item from the list.
A *drop-down combo box* (DsCdDComBox) is a combination of a text box and a drop-down list box. Users can type their choice in the text box or select an item from the list. The list is displayed only on demand – that is, users must open the control to view the list. When the list is closed, the control displays the current value.
For all the above controls, vertical and/or horizontal scroll bars are displayed when the list box is not large enough to display all items in full.

## Events
These objects can generate the following events:
EVTKEYPRESS
EVTCHANGEFOCUS
EVTSETFOCUS
EVTLISTBOXSELECT

## Attributes
| | | |
|---|---|---|
|  DsNallowMultiSelection (long)  | [CG] |  DsClistBox objects only. Indicates whether a user can select more than one item. Possible values are: TRUE Multiselection permitted. FALSE Multiselection not permitted (default).  |
|  DsNcolumns (long)  | [CSG] | The width of the list box, in characters. The default is 0. Note that DsNwidth and DsNcolumns are mutually exclusive attributes.  |
|  DsNeventMask (long)  | [CSG] | Specifies the events that the object can generate. See [select.event.input()](../events/select.event.input.md) for a list of possible masks.  |
|  DsNfontSet (long)  | [CSG] | The ID of a [DsCfontSet](dscfontset.md) object. The font object defines the font attributes to be applied to the object's text. If this attribute is not set, the Windows default font is used.  |
|  DsNheight (long)  | [G] | The height of the object, in pixels. |
|  DsNitemCount (long)  | [G] | The total number of items in the list box. This attribute is updated whenever an item is added or removed.  |
|  DsNmaxLength (long)  | [CSG] |  DsCcomBox and DsCdDComBox objects only. The maximum number of input characters in the text field. This can be any value from 0 to 4096. The default is 4096.  |
|  DsNmaxWindowSize (long)  | [CSG] | The maximum number of items the list box can contain.  |
|  DsNminWidth (long)  | [CSG] | The minimum width of the list box, in pixels. |
|  DsNminWindowSize (long)  | [CSG] | The minimum number of items the window can contain.  |
|  DsNobjectType (long)  | [G] | The object type. |
|  DsNparent (long)  | [G] | The ID of the parent object. |
|  DsNselected (long)  | [CS] |  DsClistBox objects only. This determines the state of the items specified by DsNselectedId or DsNselectionArray. Possible values are: TRUE Items are selected. FALSE Items are unselected. This attribute is valid only when DsNallowMultiSelection is TRUE.  |
|  DsNselectedId (long)  | [CSG] | The item ID of the currently selected item. An item ID of -1 causes the list box to act in a special way. In a single-selection list, all items are unselected. In a multiselection list, all items are selected or unselected, depending on the value of DsNselected.  |
| DsNselectionArray (long array) | [CSG] |  DsClistBox objects only. The item IDs of all selected items in a multiselection list. The array length is 2 * DsNselectionCount.  |
|  DsNselectionCount (long)  | [G] |  DsClistBox objects only. The number of items currently selected in a multiselection list.  |
|  DsNsetState (long)  | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md).  |
|  DsNstring (string array)  | [CSG] |  DsCcomBox and DsCdDComBox objects only. The text to be displayed in the text box. You can specify from 0 to 4096 characters. The default is an empty string.  |
| DsNstringArray | [CS] |  This contains the text and ID of each item in the list box. The data must be filled as follows: itemstring + idstring + itemstring + idstring ... All strings are null terminated.  |
|  DsNtemplate (long)  | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object.  |
|  DsNwidth (long)  | [CSG] | The width of the object, in pixels. |
|  DsNx (long)  | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent.  |
|  DsNy (long)  | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent.  |

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
