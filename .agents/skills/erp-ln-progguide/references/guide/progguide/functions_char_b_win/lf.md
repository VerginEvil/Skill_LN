# lf$()

## Syntax:
`function string lf$( [ long num_expr ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to send one or more line feeds to the screen or printer. The cursor is moved down *num_expr* lines. If you do not specify a number of lines, the cursor is moved down one line.

## Arguments
| | | |
|---|---|---|
| `[ long` | `num_expr ]` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
