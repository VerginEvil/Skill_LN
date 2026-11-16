# gbf.set.interior.icon()

## Syntax:
`function long gbf.set.interior.icon( const string icon.group(), const string unselected.closed(), const string unselected.open(), const string selected.closed(), string selected.open(), long is.default, [ const string icon.desc(), long context.menu ] )`

## Description
This function adds an interior node icon to the set of interior node icons. The return value, if non negative, must be used in subsequent [gbf.add.object()](gbf.add.object.md) calls to identify this icon set. Empty icons, in other words empty strings, are not allowed. It is not checked whether the icons are different, so for example it is allowed to have the same icon for both selected.open and selected.closed.
Note that when using the Tree Control this default icon will also be used as dummy unique root icon.
Note  In thin-client mode only the `unselected.closed` icon is used.

## Arguments
| | | |
|---|---|---|
| `const string` | `icon.group()` |  The icon.group must be a valid icon group as defined in table ttdsk900 Icon Groups using session ttdsk9100m000 Icon Groups.  |
| `const string` | `unselected.closed()` |  The unselected.closed, unselected.open, selected.closed, selected.open should be valid icons as defined in table ttdsk903 Icons using session ttdsk9103m000 Icons.  |
| `const string` | `unselected.open()` |    |
| `const string` | `selected.closed()` |    |
| `string` | `selected.open()` |    |
| `long` | `is.default` |  If set to true this icon is used as the default interior node icon and the previous default interior node icon is overruled.  |
| `[ const string` | `icon.desc() ]` |  The icon.desc should be a message that contains the description of the icon. This icon.desc will be used when the GBF tree is printed. If not given or the message is empty then nothing will be printed. Also this text will be shown when help on icons is asked for via the Help -> Icon Descriptions.  |
| `[ long` | `context.menu ]` |  The argument is used when the user wants to couple a context menu to the icon (see [gbf.create.context.menu()](gbf.create.context.menu.md)). Every icon can have it’s own context.menu. This option will be overruled by the context menu given by [gbf.add.object()](gbf.add.object.md)  |

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
