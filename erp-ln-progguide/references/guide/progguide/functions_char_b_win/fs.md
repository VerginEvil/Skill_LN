# fs$()

## Syntax:
`function string fs$( [ long num_expr ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to move the cursor *num_expr* positions to the left. If you exclude the *num_expr* argument, the cursor is moved one space to the left.

## Arguments
| | | |
|---|---|---|
| `[ long` | `num_expr ]` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
