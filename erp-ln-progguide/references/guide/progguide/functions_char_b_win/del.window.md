# del.window()

## Syntax:
`function void del.window( long wind_id )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This deletes the specified window. When you delete the current window, the next window in the internal window stack becomes the current one. The screen is not refreshed automatically.

## Arguments
| | | |
|---|---|---|
| `long` | `wind_id` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
