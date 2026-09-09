# new.window()

## Syntax:
`function long new.window( long height, long width, long row, long col )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This creates a new window. The new window automatically becomes the current window.

## Arguments
| | | |
|---|---|---|
| `long` | `height` |  The height and width of the new window.  |
| `long` | `width` |    |
| `long` | `row` |  These indicate the position of the top left corner of the new window, relative to the top left corner of the parent window.  |
| `long` | `col` |    |

## Return values
The window ID for the new window.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
