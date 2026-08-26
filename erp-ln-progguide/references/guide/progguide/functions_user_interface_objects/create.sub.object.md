# create.sub.object()

## Syntax:
`function long create.sub.object( long object, long type, [ long attribute, value [, size] ], ... )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This creates a new subobject of the specified type. The subobject is drawn on the parent window. If the parent object is destroyed, its subobjects are also destroyed.

## Arguments
| | | |
|---|---|---|
| `long` | `object` |  The ID of the parent object, as returned by [create.object()](create.object.md) when the parent object was created. The parent object is always a DsCgwindow object.  |
| `long` | `type` |  The type of subobject to be created. For example, DsCgpArc or DsCgpLine.  |
| `[ long` | `attribute, value [, size] ]` |  Use these arguments to set the subobject's attributes. For each attribute you specify, you must include the attribute type (for example, DsNgcBackground or DsNgcForeground), and the attribute value. For attributes of type void data or long array, you must also include the size of the data or array.  |
| `` | `...` |  |

## Return values
The ID for the new subobject or 0 if an error occurs. You can subsequently use the returned ID as the *sub_object_id* argument in other functions.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
