# inherit.object()

## Syntax:
`function void inherit.object( long process_nr, long object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
With this function, a process can inherit an object from its parent process. For example, a zoom process can use a pushbutton that was defined in the parent process.

## Arguments
| | | |
|---|---|---|
| `long` | `process_nr` |  The process ID of the parent process.  |
| `long` | `object_id` |  The ID of the object that must be inherited.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
