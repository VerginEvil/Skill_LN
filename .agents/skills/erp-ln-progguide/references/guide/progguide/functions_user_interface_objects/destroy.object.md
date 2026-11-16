# destroy.object()

## Syntax:
`function void destroy.object( long object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This removes the specified object and all its children (if any).

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  The object ID, as returned by [create.object()](create.object.md) when the object was created.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
