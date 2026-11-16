# insch$()

## Syntax:
`function string insch$( string attr )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to insert the result of *string_expr* at the current cursor position. The characters to the right of the cursor are moved *string_expr* positions to the right.

## Arguments
| | | |
|---|---|---|
| `string` | `attr` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
