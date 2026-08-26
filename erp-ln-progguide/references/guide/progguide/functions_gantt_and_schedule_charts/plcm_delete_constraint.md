# plcm.delete.constraint

## Syntax:
`function long plcm.delete.constraint( string activity.id.from, string activity.id.to, long constraint.type )`

## Description
Deletes a constraint between two activities.

## Arguments
| | | |
|---|---|---|
| `string` | `activity.id.from` |  ID of the from activity.  |
| `string` | `activity.id.to` |  ID of the to activity  |
| `long` | `constraint.type` |  CONSTRAINT_START_START | CONSTRAINT_START_END | CONSTRAINT_END_START | CONSTRAINT_END_END  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Synopsis](synopsis.md)
- [Example](example.md)
