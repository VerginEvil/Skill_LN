# get.sub.object()

## Syntax:
`function long get.sub.object( long object, long sub_object_id, [ long attribute, ref void value, ref long size ] )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about a specified subobject.

## Arguments
| | | |
|---|---|---|
| `long` | `object` |  The ID of the parent object, as returned by [create.object()](create.object.md) when the object was created.  |
| `long` | `sub_object_id` |  The ID of the subobject of the specified parent object.  |
| `[ long` | `attribute ]` |  The attribute you want to retrieve (for example, DsNgcBackground or DsNgcForeground).  |
| `[ ref void` | `value ]` |  This returns the current value of the specified attribute.  |
| `[ ref long` | `size ]` |  For attributes of type void data and long array, this returns the size of the data or array.  |

## Return values
TRUE success
FALSE error

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
