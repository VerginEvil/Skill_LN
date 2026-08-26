# plcm.constraint.deleted

## Syntax:
`function boolean plcm.constraint.deleted( const string activity.id.from, const string activity.id.to, const long constraint.type )`

## Description
Callback-function for when the constraint is about to be deleted in the UI.

## Arguments
| | | |
|---|---|---|
| `const string` | `activity.id.from` |  ID of the from activity.  |
| `const string` | `activity.id.to` |  ID of the to activity.  |
| `const long` | `constraint.type` |  CONSTRAINT_START_START | CONSTRAINT_START_END | CONSTRAINT_END_START | CONSTRAINT_END_END  |

## Return values
True, when the delete is allowed.
False, when the delete is not allowed.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
