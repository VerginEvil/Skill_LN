# DsCradioBox

## Description
A DsCradioBox object is an instance of DsCrowColumn object that contains radio buttons (also referred to as option buttons).

## Events
A DsCradioBox object does not generate events.

## Attributes
| | | | |
|---|---|---|---|
| DsNfixedDimension (long) | [CSG] | Specifies how children are arranged in the radio box. Possible values are: |  |
| DSVERTICAL | Children are arranged vertically, from top to bottom. Use DsNnumRows to specify the maximum number of children that can be displayed vertically. |  |  |
|  |  | DSHORIZONTAL | Children are arranged horizontally, from left to right. Use DsNnumColumns to specify the maximum number of children that can be displayed horizontally. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |  |
| DsNnumColumns (long) | [CSG] | The maximum number of children that the object can display horizontally. |  |
| DsNnumRows (long) | [CSG] | The maximum number of children that the object can display vertically. |  |
| DsNobjectType (long) | [G] | The object type. |  |
| DsNpacking (long) | [CSG] | The method of spacing the radio buttons within the radio box. Possible values are: |  |
| DSPACKTIGHT | The radio box contains cells of equal size, set to the size of the largest child window. Child windows positioned within these cells maintain their minimum dimensions. This is the default value. |  |  |
|  |  | DSPACKEQUAL | The radio box contains cells of equal size, set to the size of the largest child window. All child windows within these cells are displayed at the size of the largest child window. |
|  |  | DSPACKNONE | Child windows determine their own size and position. The radio box window is sized to accommodate all its children. |
|  |  | DSPACKSTACKED | All child windows have the same size and position. Only the last created child is visible. All other children are stacked beneath this. |
| DsNparent (long) | [G] | The ID of the parent object. |  |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |  |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |  |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |  |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |  |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |  |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
