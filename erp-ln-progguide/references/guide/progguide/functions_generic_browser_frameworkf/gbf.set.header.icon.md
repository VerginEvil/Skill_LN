# gbf.set.header.icon()

## Syntax:
`function long gbf.set.header.icon( const string icon.group(), const string icon(), long is.default, [ const string icon.desc() ] )`

## Description
Adds a header node icon to the set of header node icons. The value, if non negative, which is returned must be used in subsequent calls to identify this icon set. Empty icons, in other words empty strings, are not allowed.

## Arguments
| | | |
|---|---|---|
| `const string` | `icon.group()` |  The icon.group must be a valid icon group as defined in table ttdsk900 Icon Groups using session ttdsk9100m000 Icon Groups.  |
| `const string` | `icon()` |  Also the icon should be a valid icon as defined in table ttdsk903 Icons using session ttdsk9103m000 Icons.  |
| `long` | `is.default` |  If set to true this icon is used as the default header icon and the previous default header icon is overruled.  |
| `[ const string` | `icon.desc() ]` |  The icon.desc should be a message containing the description of the icon. This icon.desc will be used when the GBF tree is printed. If not given or the message is empty then nothing will be printed. Also this text will be shown when help on icons is asked for via the Help -> Icon Descriptions.  |

## Return values
| | |
|---|---|
| > 1 | The identification of this new icon set |
| 1 | Should never be returned, as 1 is the GBF default |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ICON.EMPTY | Empty icon strings are not allowed |
| GBF.ICON.LOAD.ERROR | Could not load the icon |
| GBF.ILL.BITMAP | Illegal bitmap for icon (not a GIF file) |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
