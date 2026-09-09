# move.window()

## Syntax:
`function void move.window( long col, long row )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This moves the current window to a specified position (relative to the top left corner of the parent window). There is no need to refresh the window.

## Arguments
| | | |
|---|---|---|
| `long` | `col` |    |
| `long` | `row` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
