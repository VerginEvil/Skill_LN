# last.window()

## Syntax:
`function void last.window( long wind_id )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This places the specified window below all other windows on the screen. The window is also placed at the last position in the internal window stack. The alterations become visible on screen only when you call [refresh()](refresh.md) or [wrebuild()](wrebuild.md).

## Arguments
| | | |
|---|---|---|
| `long` | `wind_id` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
