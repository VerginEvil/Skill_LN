# gbf.set.menu.head()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.menu.head( string menu.text, [ long maskbit, long multi.mask ] )`

## Description
Adds a menu header to the menu bar.
The value returned is to be used in subsequent [gbf.set.menu.item()](gbf.set.menu.item.md) functions calls to add new menu items to this menu.
The number of menus is limited, currently fixed to 10. Note that the default menus are included (see [gbf.init()](gbf.init.md)) if they must be generated.

## Arguments
| | | |
|---|---|---|
| `string` | `menu.text` |  The menu.text should be a message. In this case the message is first translated to its actual value. So for example when menu.text is “ttgbfl0006” then this value will be: “File”. See also: [gbf.set.menu.item()](gbf.set.menu.item.md). The rest of this section keeps using the menu.text as if this is the actual menu header text.  |
| `[ long` | `maskbit ]` |  The maskbit can be used to disable a menu head depending on the menumask set with [gbf.add.object()](gbf.add.object.md). The default value is 0.  |
| `[ long` | `multi.mask ]` |  The multi.mask is used to indicate what should happen when zero or more than one objects are selected. The least significant bit (lsb) is used to indicate whether the menu head should be disabled when no objects are selected. The second bit is used to indicate whether the menu head should be disabled when more than one objects are selected. The default value is GBF.ZERO.ENABLE + GBF.MULTI.ENABLE. The following defines should be used: · · GBF.ZERO.ENABLE menu head is enabled when zero objects are selected · · GBF.ZERO.DISABLE menu head is disabled when zero objects are selected · · GBF.MULTI.ENABLE menu head is enabled when more than one object is selected · · GBF.MULTI.DISABLE menu head is disabled when more than one object is selected  |

## Return values
| | |
|---|---|
| > 0 | The identification of this new menu head |
| GBF.NO.MEMORY | Not enough memory |
| GBF.MENU.EMPTY | Empty menu text is not allowed |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.MAX.MENU | Too many menus defined |

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
