# destroy.sub.object()

## Syntax:
`function void destroy.sub.object( long object, long sub_object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This removes the specified subobject.

## Arguments
| | | |
|---|---|---|
| `long` | `object` |  The ID of the parent object, as returned by [create.object()](create.object.md) when the parent object was created.  |
| `long` | `sub_object_id` |  The ID of the subobject, as returned by [create.sub.object()](create.sub.object.md) or [create.sub.object.by.id()](create.sub.object.by.id.md) when the subobject was created.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
