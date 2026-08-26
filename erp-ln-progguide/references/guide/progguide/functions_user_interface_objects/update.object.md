# update.object()

## Syntax:
`function void update.object( long object_id )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This (re)draws the specified object. Some changes made to DsCgwindow and DsCbarMenu objects are stored internally and become visible only after an *update.object()* call. You must also call this function to make new DsCmwindow and DsCgwindow objects visible.

## Arguments
| | | |
|---|---|---|
| `long` | `object_id` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [User interface objects overview](overview.md)
- [User interface objects synopsis](synopsis.md)
- [User interface objects: example](example.md)
