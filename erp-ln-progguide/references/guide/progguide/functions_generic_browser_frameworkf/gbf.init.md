# gbf.init()

## Syntax:
`#include <bic_gbf>`
`function long gbf.init( const string library(), const string title(), [ long default.menu, long default.button, long default.options, long standard.buttons, long default.context ] )`

## Description
This function must be the first to be called, it initializes the global data structures of the GBF. It is not forbidden to reactivate a new run of the GBF in a session after a previous run of the GBF has terminated, the GBF has to clear its global variables again. This cleaning of the global variables cannot be done when leaving the GBF as at that point in time it must still be possible to get some information about the settings in order for the application to save and restore some user preferences, see for example [gbf.get.refresh.strategy()](gbf.get.refresh.strategy.md) and [gbf.get.sort.strategy()](gbf.get.sort.strategy.md).

## Arguments
| | | |
|---|---|---|
| `const string` | `library()` |  The library should be the name of the library, in general this is the application itself, which may or should contain the following call back functions (see [gbf.current.library()](gbf.current.library.md) and [gbf.file.to.library()](gbf.file.to.library.md) for an easy way to retrieve the library name):  |
| `const string` | `title()` |  The title will be the title of the window. It may be empty, in which case the window will have the following title: <session.desc> [User: <user.name>] or: <prog.name>: <session.desc> [User: <user.name>] where  |
| `[ long` | `default.menu ]` |  The flag default.menu specifies which of the following standard menus the browser will have (the words in *italic* are the actual menu text, taken from the message catalogue)  |
| `[ long` | `default.button ]` |  The flag default.button specifies which of the following standard buttons the browser will have:  |
| `[ long` | `default.options ]` |  The flag default.options specifies further configuration of the Generic Browser Framework:  |
| `[ long` | `standard.buttons ]` |  The standard.button indicate which standard GBF buttons and menu items are further handled by the application. This means that the GBF will create menu items and buttons for these buttons, and call the application to perform the actual operation, see [gbf.menu.selected()](gbf.menu.selected.md). When no standard.button is given (so the [gbf.init()](gbf.init.md) is called with at most 5 arguments) then 0 is used as the current value for standard.button. These buttons are:  |
| `[ long` | `default.context ]` |  With this option a default context menu can be defined. The context menu behaves like the standard buttons and the standard menu. Again, these menu items are coupled with the item in the menu.bar and the toolbar. The following options can be used for the context menu:  |

## Return values
| | |
|---|---|
| 0 | Success |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |
| GBF.NO.GRAPHICS | GBF can only run on graphical displays, not on ASCII only displays  |
| GBF.NO.MEMORY | Not enough memory |

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
