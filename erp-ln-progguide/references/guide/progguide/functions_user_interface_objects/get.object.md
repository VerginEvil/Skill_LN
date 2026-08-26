# get.object()

## Syntax:
`function long get.object( long object_id, long attribute, void value, long size )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about a specified object.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The object ID, as returned by [create.object()](create.object.md) when the object was created.  |
| `long` | `attribute` |  The attribute you want to retrieve (for example, DsNtitle or DsNbackground).  |
| `void` | `value` |  This returns the current value of the specified attribute.  |
| `long` | `size` |  For attributes of type void data and long array, this returns the size of the data or array.  |

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
