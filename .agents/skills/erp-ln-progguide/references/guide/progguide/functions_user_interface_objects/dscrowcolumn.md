# DsCrowColumn

## Description
A DsCrowColumn object is a container object that displays its children in rows and columns.

## Events
A DsCrowColumn object does not generate events.

## Attributes
| | | | |
|---|---|---|---|
| DsNfixedDimension (long) | [CSG] | Specifies how children are arranged in the object. Possible values are: |  |
| DSVERTICAL | Children are arranged vertically, from top to bottom. Use DsNnumRows to specify the maximum number of children that can be displayed. |  |  |
|  |  | DSHORIZONTAL | Children are arranged horizontally, from left to right. Use DsNnumColumns to specify the maximum number of children that can be displayed. |
| DsNheight (long) | [CSG] | The height of the object, in pixels. |  |
| DsNhspace (long) | [CSG] | The horizontal spacing (in pixels) between child objects and between the edge of the DsCrowColumn object and its nearest child. |  |
| DsNinferiorPointerCursor (long) | [CSG] | The shape of the inferior mouse pointer when positioned over the object. A child of a DsCrowColumn object inherits this mouse pointer, unless otherwise specified. This attribute is overruled by a DsNsuperiorPointerCursor attribute set for the object itself or for ancestor windows. It is also overruled by a DsNinferiorPointerCursor setting in descendant windows. Possible values are: DSCDEFAULT (default) DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP |  |
| DsNjustify (long) | [CSG] | The justification of child windows within the cells of the DsCrowColumn object. This is relevant only when DsNpacking is set to DSPACKTIGHT. The possible values for horizontal justification are: DSJUSTIFY LEFT (default) DSJUSTIFY CENTER DSJUSTIFY RIGHT The possible values for vertical justification are: DSJUSTIFYTOP (default) DSJUSTIFYMIDDEL DSJUSTIFYBOTTOM When setting this attribute, you must combine a horizontal justification option and a vertical justification option. |  |
| DsNnumColumns (long) | [CSG] | The maximum number of children that the object can display horizontally. |  |
| DsNnumRows (long) | [CSG] | The maximum number of children that the object can display vertically. |  |
| DsNobjectType (long) | [G] | The object type. |  |
| DsNpacking (long) | [CSG] | The method of spacing the child objects within the DsCrowColumn object. Possible values are: |  |
| DSPACKTIGHT | The object contains cells of equal size, set to the size of the largest child window. Child windows positioned within these cells maintain their minimum dimensions. This is the default value. |  |  |
|  |  | DSPACKEQUAL | The object contains cells of equal size, set to the size of the largest child window. All child windows within these cells are displayed at the size of the largest child window. |
|  |  | DSPACKNONE | Child windows determine their own size and position. The DsCrowColumn window is sized to accommodate all its children. |
|  |  | DSPACKSTACKED | All child windows have the same size and position. Only the last created child is visible. All other children are stacked beneath this. |
| DsNparent (long) | [G] | The ID of the parent object. |  |
| DsNsetState (long) | [CS] | The state of the object. See [DsCmwindow](dscmwindow.md). |  |
| DsNsuperiorPointerCursor (long) | [CSG] | The shape of the superior mouse pointer when positioned over the object. A child of a DsCrowColumn object always inherits this mouse pointer. DsNsuperiorPointerCursor overrules any inferior mouse pointer (DsNinferiorPointerCursor) set for the object and all mouse pointers set for descendant windows. Possible values are: DSCDEFAULT DSCPENCIL DSCARROW DSCQUESTIONARROW DSCCROSSHAIR DSCSPLITHORIZONTAL DSCFLEUR DSCSPLITVERTICAL DSCHAND DSCSPRAYCAN DSCMAGNIFY DSCWATCH DSCAPPSTARTING DSCNODROP |  |
| DsNvspace (long) | [CSG] | The vertical spacing (in pixels) between child objects and between the and between the edge of the DsCrowColumn object and its nearest child. |  |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the object. |  |
| DsNwidth (long) | [CSG] | The width of the object, in pixels. |  |
| DsNx (long) | [CSG] | The x-coordinate of the object's outer left edge, in pixels, relative to the inner left edge of its parent. |  |
| DsNy (long) | [CSG] | The y-coordinate of the object's outer top edge, in pixels, relative to the inner top edge of its parent. |  |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
