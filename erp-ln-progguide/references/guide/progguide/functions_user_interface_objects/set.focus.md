# set.focus()

## Syntax:
`function void set.focus( long object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This moves the keyboard input focus to the specified object. When an object has input focus, all keyboard input within the object's main window is received by that object, regardless of the position of the cursor. When an object has input focus, it is surrounded by a rectangular highlight.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)

- [User interface objects synopsis](synopsis.md)

- [User interface objects: example](example.md)
