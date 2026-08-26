# refresh()

## Syntax:
`function void refresh( [ long wind_id ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This copies the internal screen to the terminal screen. The internal screen is modified by any function which sends data to the screen (for example, *print()*, *box()*, *map.window()*). The terminal screen is updated only after you call *refresh()*.
If you specify a window ID, the specified window is refreshed. But the window sequence is not changed. If you do not specify a window ID, the current window is refreshed and placed above all other windows on the screen.

## Arguments
| | | |
|---|---|---|
| `[ long` | `wind_id ]` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
