# gbf.set.menu.item()

## Syntax:
`function long gbf.set.menu.item( long menu.id, const string menu.text(), const string keystroke(), [ long is.default, long menu.function.id ], long maskbit, [ long multi.mask ], long std.button )`

## Description
Adds a menu item to the set of menu items under the heading as identified by menu.id, as well as it allows to assign a keystroke combination (such as <Ctrl>+A and so on.) and connect it to a standard GBF button which the GBF does not service itself.

## Arguments
| | | |
|---|---|---|
| `long` | `menu.id` |  The menu identification.  |
| `const string` | `menu.text()` |  Both menu.text and keystroke should be messages. In this case the message is first translated to its actual value. So for example when menu.text is “ttgbfl0006” then this value will be: “File”. The reason why messages are preferred over (hard coded) text is that help associated to that message will be called when the context help is asked for for this menu or keystroke. The rest of this section keeps using the menu.text and keystroke as if these are the actual menu texts and keystrokes. At least menu.text or keystroke must be specified: · · If the menu.text is “---” (3 minutes) then only a menu separator line is drawn in the menu which can never be selected and will generate a 0 return value. Note that the keystroke should be empty in this case. Also only BW supports these menu separator lines, but no error is generated when using this under BX. Note that for these menu separator also the function gbf.set.menu.separator() should be used. · · If the menu.text is non empty then the menu.id must be a value returned by a preceding gbf.set.menu.head() call.  |
| `const string` | `keystroke()` |  The keystroke may be empty, in which case no special keystroke recognition is done for this menu item. The keystroke will be added to the menu on the right hand side of the menu entry. The first character in the menu.id which is preceded by an ‘&’ will become underscored which allows you to select that menu item by typing that underscored character at the moment the menu is dropped down. This however is not considered to be a keystroke in this manual. · · If the menu.text is empty, then the keystroke is added to an anonymous menu (menu.id is ignored in this case). The return value of this function (if > 0) will be the value that is used when the menu is activated or the keystroke is recognized. The GBF does not check whether this keystroke is already in use (when the specified keystroke is not empty), and it is left undetermined which value will be given when the keystroke is recognized, in this ambiguous case. The format of the keystroke is: [Ctrl+][Shift+][Alt+](<single char>|F<nr>|<special key>) where:  |
| `[ long` | `is.default ]` |  The is.default argument indicates whether (if the value is true) or not (if the value is false) to use this menu item as the default action. That is when double clicking on a leaf node or selecting and <Enter> (if it could successfully be added) as the default leaf node icon set. The default value is false. When a menu item is selected or the keystroke is recognized, the following application function will be called by default: gbf.menu.selected(string object.key, long object.value, long menu.option) Where menu.option is the return value from the [gbf.set.menu.item()](gbf.set.menu.item.md) function call. For further details about this function see [gbf.menu.selected()](gbf.menu.selected.md). When another function has been defined to be called, that function will be called instead, but the arguments will be the same.  |
| `[ long` | `menu.function.id ]` |  The menu.function.id indicates, if > 0, the function to be called when the menu item is selected or keystroke is recognized, instead of the default function. This menu.function.id must be a value returned by a preceding gbf.set.menu.function() call. The default value is 0.  |
| `long` | `maskbit` |  If the maskbit is used in the menumask of the currently selected item the menu item will be disabled. The default value is 0.  |
| `[ long` | `multi.mask ]` |  The multi.mask is used to indicate what should happen when zero or more than one objects are selected. The lsb is used to indicate whether the menu item should be disabled when no objects are selected. The second bit is used to indicate whether the menu item should be disabled when more than one objects are selected. The default value is GBF.ZERO.ENABLE + GBF.MULTI.ENABLE. The following defines should be used:  |
| `long` | `std.button` |  The optional argument std.button should no longer be used. It is only here for compatibility reasons with older versions of the GBF. It is strongly advised to use the new mechanism (see flag standard.button of [gbf.init()](gbf.init.md)):  |

## Return values
| | |
|---|---|
| > 1 | The identification of this new menu entry |
| 1 | Should never be returned, as 1 is the GBF default  |
| 0 | Menu separator line added |
| GBF.NO.MEMORY | Not enough memory |
| GBF.MENU.EMPTY | Empty menu text is not allowed |
| GBF.ILL.MENU.ID | Illegal menu.id value |
| GBF.ILL.FUNCTION | Illegal menu.function.id value |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |
| GBF.MAX.MENU | Too many submenus for this menu defined |

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
