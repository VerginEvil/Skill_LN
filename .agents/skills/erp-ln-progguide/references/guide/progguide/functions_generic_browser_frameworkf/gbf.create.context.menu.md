# gbf.create.context.menu()

## Syntax:
`function long gbf.create.context.menu( )`

## Description
This function creates a popup menu that is activated when the user clicks on the right mouse button and the mouse cursor is on a node. The popup menu is initially completely empty. The programmer has to add the popup menu items with the function [gbf.set.menu.item()](gbf.set.menu.item.md). After that, the developer has to bind this context menu to a certain object through a call to [gbf.add.object()](gbf.add.object.md) which has an argument *context.menu.id* for this so at the same time the node is created the context menu is assigned to it. Thus each node can have its own specific context menu.
The behavior of each menu item is determined by the programmer who binds a function to the entry with the function [gbf.set.menu.function()](gbf.set.menu.function.md).
The function gbf.create.context.menu() has to be called before the call to [gbf.start()](gbf.start.md).

## Return values
| | |
|---|---|
| >= 0 | Successful completion, returned value is the new popup menu.id |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.NOT.EXPECTED | Function called when GBF did not expect it |

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
