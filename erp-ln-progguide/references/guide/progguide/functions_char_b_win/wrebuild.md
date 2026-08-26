# wrebuild()

## Syntax:
`function void wrebuild( long mode )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This redraws the entire screen. The *mode* argument can have one of the following values:
| | |
|---|---|
| 0 | All windows are refreshed. |
| 1 | The screen is cleared and all windows are rebuilt.  |

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
