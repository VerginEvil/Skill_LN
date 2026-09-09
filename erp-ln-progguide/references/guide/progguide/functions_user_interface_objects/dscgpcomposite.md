# DsCgpComposite

## Description
A DsCgpComposite subobject groups a number of graphical parts so that you can manipulate them as a single unit. The parent object is always a DsCgwindow object.

## Events
A DsCgpComposite object does not generate events.

## Attributes
| | | |
|---|---|---|
| DsNattribute (long) | [CSG] | The status of the subobject. Possible values are: GPNORMAL Detectable and visible. GPUNDETECTABLE Cannot be detected with *query.object()*. GPINVISIBLE Subobject is hidden. |
| DsNheight (long) | [G] | The height of the object, in pixels. |
| DsNobjectType (long) | [G] | The object type. |
| DsNrefSubObject (long) | [CS] | The ID of the subobject used as a reference by DsNsequence. |
| DsNsequence (long) | [CS] | The position of the composite object relative to the reference object. Possible values are: GPMKFIRST Part is drawn above all other parts. GPMKLAST Part is drawn under all other parts. GPMKNEXT Part is drawn under DsNrefSubObject. GPMKPREV Part is drawn above DsNrefSubObject. |
| DsNsubObjectArray (long array) | [CSG] | The IDs of the subobjects that the group contains. This attribute takes two values. The first contains the name of the subobject array, the last specifies the number of subobjects the group contains. |
| DsNtemplate (long) | [CS] | The ID of a [DsCtemplate](dsctemplate.md) that defines a set of attributes to be applied to the subobject. |
| DsNwidth (long) | [G] | The width of the subobject, in pixels. |
| DsNx (long) | [CSG] | The x-coordinate of the subobject's outer left edge, in pixels, relative to the inner left edge of its parent. |
| DsNy (long) | [CSG] | The y-coordinate of the subobject's outer top edge, in pixels, relative to the inner top edge of its parent. |

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
