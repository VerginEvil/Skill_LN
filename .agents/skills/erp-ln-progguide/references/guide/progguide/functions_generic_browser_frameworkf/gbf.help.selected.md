# gbf.help.selected()

## Syntax:
`#include <bic_gbf>`
`function void gbf.help.selected( long obj.id, const string object.key(), long object.value, long help.value )`

## Description
This function will be called when the object has been selected followed by a menu selection or a keystroke.
There are three possibilities for obj.id:
| | |
|---|---|
| obj.id < 0 | More that one object was currently selected when this menu item was chosen and obj.id contains the negative number of selected objects, that is: -obj.id is the actual number of selected objects. So obj.id in this case is NO valid object identification, but on the other hand object.key and object.value contain the identification of the first selected object. All currently selected objects can be obtained using a [gbf.get.selected()](gbf.get.selected.md) for each selected object. This case will only happen if the GBF is configured to support multiple select (see [gbf.init()](gbf.init.md)) |
| obj.id = 0 | No object was currently selected when this menu entry was chosen, and object.key will be an empty string, that is isspace(object.key) is true. |
| obj.id > 0 | Precisely one object was currently selected when this menu item was chosen and that object is identified by obj.id as well as by the object.key and object.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call. The given obj.id identifies the object for the GBF and should be used only as object identification for other GBF functions. |
The help.value identifies which help entry was chosen and what the end-user probably wants help on:
| | | |
|---|---|---|
| Contents | GBF.MENU.HELP.CONT | give a table of contents of all available help within the current session that is using the GBF |
| What’s This? | GBF.MENU.HELP.SRCH | Starts the context sensitive help |
| Using Session | GBF.MENU.HELP.SESS | Give help of how to use the current session which is build using the GBF |
The return value of this function is ignored, as it does not influence the normal flow of control of the application.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  See above.  |
| `const string` | `object.key()` |    |
| `long` | `object.value` |    |
| `long` | `help.value` |    |

## Return values
None

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
