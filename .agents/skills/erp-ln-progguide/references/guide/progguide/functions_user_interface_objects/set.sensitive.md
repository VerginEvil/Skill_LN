# set.sensitive()

## Syntax:
`function void set.sensitive( long object_id, long status )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This sets the sensitivity of a specified object.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The ID of the object.  |
| `long` | `status` |  The status that must be set for the object. Possible values are: DSSETSENSITIVE DSSETINSENSITIVE When the status of an object is set to insensitive, the object and its children are disabled.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
