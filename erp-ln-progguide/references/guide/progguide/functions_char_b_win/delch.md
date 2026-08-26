# delch$()

## Syntax:
`function string delch$( long num_expr )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to delete *num_expr* characters, from the current cursor position to the right. The text following the deleted characters shifts *num_expr* positions to the left.

## Arguments
| | | |
|---|---|---|
| `long` | `num_expr` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
