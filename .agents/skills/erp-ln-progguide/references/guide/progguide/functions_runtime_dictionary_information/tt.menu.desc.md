# tt.menu.desc()

## Syntax:
`function string tt.menu.desc( string menu(13), string par_menu, [ ref string desc() mb ] )`

## Description
This returns information about a specified menu. It is returned, and optionally also stored in the *desc* argument. (The optional argument is only present for backward compatibility.)

## Arguments
| | | |
|---|---|---|
| `string` | `menu(13)` |  The menu name.  |
| `string` | `par_menu` |  In the case of parallel menus, specify the menu sequence number here. Otherwise, enter 1.  |
| `[ ref string` | `desc() mb ]` |  This returns the description (in the user's current language) of the specified menu.  |

## Return values
The description is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
desc = tt.menu.desc( "tfgld0000m000", "1" )

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
