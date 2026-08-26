# resize.window()

## Syntax:
`function void resize.window( long width, long height )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This resizes the current window. You must specify the new width and height in pixels. There is no need to refresh the window.

## Arguments
| | | |
|---|---|---|
| `long` | `width` |  |
| `long` | `height` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
