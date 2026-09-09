# cs$()

## Syntax:
`function string cs$( [ long num_expr ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to change the window size and/or clear the window. The *num_expr* argument can have one of the following values:
| | |
|---|---|
| 0 | clear current window |
| 1 | clear current window (default value) |
| 2 | set screen to 80 columns and clear current window |
| 3 | set screen to 132 columns and clear current window |
| 4 | set screen to 80 columns without clearing current window |
| 5 | set screen to 132 columns without clearing current window |

## Arguments
| | | |
|---|---|---|
| `[ long` | `num_expr ]` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
