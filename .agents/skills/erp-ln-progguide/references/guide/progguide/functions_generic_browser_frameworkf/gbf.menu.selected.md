# gbf.menu.selected()

## Syntax:
`#include <bic_gbf>`
`function long gbf.menu.selected( long obj.id, const string object.key(), long object.value, long menu.option )`

## Description
This function will be called when the object has been selected followed by a menu selection or a keystroke.
obj.id
There are three possibilities for obj.id:
| | |
|---|---|
| obj.id < 0 | More that one object was currently selected when this menu item was chosen and obj.id contains the negative number of selected objects, that is: -obj.id is the actual number of selected objects. So obj.id in this case is NO valid object identification, but on the other hand object.key and object.value contain the identification of the first selected object. All currently selected objects can be obtained using a [gbf.get.selected()](gbf.get.selected.md) for each selected object. This case will only happen if the GBF is configured to support multiple select (see [gbf.init()](gbf.init.md)) |
| obj.id = 0 | No object was currently selected when this menu entry was chosen, and object.key will be an empty string, that is isspace(object.key) is true. |
| obj.id > 0 | Precisely one object was currently selected when this menu item was chosen and that object is identified by obj.id as well as by the object.key and object.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call. The given obj.id identifies the object for the GBF and should be used only as object identification for other GBF functions like [gbf.get.parent()](gbf.get.parent.md), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and gbf.update.object(). |
menu.option
The selected menu item or keystroke is identified by the given menu.option, which has been returned by the GBF on a preceding gbd.set.menu.item() call or is one of the standard GBF buttons and menu items which are supported by the application (see argument standard.button of [gbf.init()](gbf.init.md)). The following table suggests what the application should do on these standard buttons:
| | |
|---|---|
| Menu option | Description |
| GBF.BUTTON.COPY | Copy the current selected object(s) |
| GBF.BUTTON.CUT | Cut (delete) the current selected object(s) |
| GBF.BUTTON. DELETE | Delete the current selected object(s) |
| GBF.BUTTON.GRP. NEW | Insert a new group object |
| GBF.BUTTON.INSERT | Insert a new object |
| GBF.BUTTON.PASTE | Paste the contents of the cut/copy buffers into the current selected object |
| GBF.BUTTON.TEXT | Start the text editor for the current selected object(s) |
| GBF.BUTTON.UNDO | Undo the last operation |
Note that the GBF will never delete objects by itself. So even after a GBF.BUTTON.CUT and/or GBF.BUTTON.DELETE action still a GBF.DO.DELETE.CURRENT (see below) must be returned. When the menu.option is GBF.BUTTON.COPY or GBF.BUTTON.CUT then the current selected object(s) are already stored in the so called Cut, Copy & Paste buffers, so there is no need to return a GBF.DO.CUTCOPY.INSERT return flag in these cases. Of course a return value of GBF.DO.CUTCOPY.CLEAR will indeed clear this buffer, even on this Cut or Copy operation.
After the application has been finished, the return value of this function to GBF will inform GBF what to do. There are a number of return categories defined, each having a number of different options. One flag of each group should be used to construct the full return value. These flags can be added (‘+’) or bitwise ‘or’ed.

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  See above.  |
| `const string` | `object.key()` |    |
| `long` | `object.value` |    |
| `long` | `menu.option` |    |

## Return values
| | | |
|---|---|---|
| category | define | description |
| redraw | GBF.DO.REDRAW.TREE | redraw the whole tree |
| refresh | GBF.DO.REFRESH.NONE | no refresh needed |
|  | GBF.DO.REFRESH.CURRENT | refresh everything under the current selected object |
|  | GBF.DO.REFRESH.LEVEL | refresh level on which current selected object resides |
|  | GBF.DO.REFRESH.TREE | refresh the whole tree |
| restart | GBF.DO.RESTART.NONE | no restart needed |
|  | GBF.DO.RESTART.CURRENT | restart everything under the current selected object |
|  | GBF.DO.RESTART.LEVEL | restart level or which current selected object resides |
|  | GBF.DO.RESTART.TREE | restart the whole tree |
| cut,. copy | GBF.DO.CUTCOPY.NONE | do nothing with the cut, copy paste buffers |
| & paste | GBF.DO.CUTCOPY.CLEAR | clear the cut, copy and paste buffers |
|  | GBF.DO.CUTCOPY.INSERT | replace the contents of the cut, copy and clear buffers with the current selected objects Note: not needed after a GBF.BUTTON.CUT or GBF.BUTTON.COPY menu.option. |
| delete | GBF.DO.DELETE.NONE | do not delete object |
|  | GBF.DO.DELETE.CURRENT | delete this occurrence of object, and if interior node all underlying nodes in this tree only |
|  | GBF.DO.DELETE.GLOBAL | delete all occurrences of object from tree, and if interior node all underlying nodes in these trees only |
| level | GBF.DO.LEVEL.NONE | do not open or close anything |
|  | GBF.DO.LEVEL.OPEN | open level only done for closed interior node, no operation in all other cases |
|  | GBF.DO.LEVEL.CLOSE | close level only done for open interior node, no operation in all other cases |
| terminate | GBF.DO.CONTINUE | continue normal processing |
|  | GBF.DO.ABORT | abort GBF, which will end the GBF and return with an error, see [gbf.start()](gbf.start.md) |
|  | GBF.DO.EXIT | finish GBF, which will end the GBF and return with 0, see [gbf.start()](gbf.start.md) |
|  | GBF.DO.NOT.EXIT | continue with processing (do NOT stop the GBF) rather than stopping. This should only be used when: gbf.save(…,…,…, GBF.MENU.FILE.QUIT) has been called. |
The defines will be chosen such that a value of 0 means: do nothing special (not even a redraw or refresh of current object). In general all the above groups are mutual exclusive, that is using a member of one group does not affect using members from any other group. The only exception is that a member of the *refresh* group is ignored when a member of the *restart* group (other than GBF.DO.RESTART.NONE) is used.
In case of a multiple select, these options apply to all currently selected items except when one of the *refresh* or *restart* categories is used, as in this case always GBF.DO.REFRESH.TREE or GBF.DO.RESTART.TREE is used.
The difference between GBF.DO.RESTART.TREE and GBF.DO.REFRESH.TREE is that a

- GBF.DO.REFRESH.TREE tries to keep the current view as similar as it is now on the screen. This is merge the (new) data from the application with which is already available in the GBF, and delete unretrieved data

- GBF.DO.RESTART.TREE restarts the GBF from fresh, that is as if a [gbf.start()](gbf.start.md) has been executed, but see also: gbf.get.read.level() and gbf.set.read.level().

When no object is currently selected then also the GBF.DO.REFRESH.CURRENT and GBF.DO.REFRESH.LEVEL behave the same as a GBF.DO.REFRESH.TREE (refresh the whole tree). Similar when no object is currently selected then also the GBF.DO.RESTART.CURRENT and GBF.DO.RESTART.LEVEL behave the same as a GBF.DO.RESTART.TREE (restart the whole tree).
The difference between GBF.DO.REFRESH.CURRENT (or GBF.DO.REFRESH.LEVEL) is that the first one refreshes (or restarts) everything under the current selected object, excluding the current object, and the latter does a refresh (or restarts) on the parent object of the current selected object. So a GBF.DO.REFRESH.LEVEL does not refresh that parent, but refreshes all of its children, which includes the current selected object and all of its brother objects. Note that the current selected object can be updated using gbf.update() functions. The same applies to GBF.DO.RESTART.CURRENT and GBF.DO.RESTART.LEVEL.

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
