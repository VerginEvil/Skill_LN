# tt.menu.present()

## Syntax:
`function boolean tt.menu.present( string menu(13), string par_menu )`

## Description
This checks if the specified menu of the current package is present in the runtime dictionary.

## Arguments
| | | |
|---|---|---|
| `string` | `menu(13)` |  The menu name.  |
| `string` | `par_menu` |  In the case of parallel menus, specify the menu sequence number here. Otherwise, enter 1.  |

## Return values
false error; menu not found
true success

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
