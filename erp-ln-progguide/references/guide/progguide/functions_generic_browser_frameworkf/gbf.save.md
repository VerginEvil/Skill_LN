# gbf.save()

## Syntax:
`function long gbf.save( long obj.id, const string object.key(), long object.value, long save.type )`

## Description
This function will be called when the Save or Save+Exit menu has been called. The idea is that the main application should now save any unsaved data.
The save.type indicates for what reason this function is called. The possible values are:
| | | | |
|---|---|---|---|
| Value | Menu item selected | Keystroke given | Button pressed |
| GBF.MENU.FILE.SAVE | Save | Ctrl+S | Save (floppy disk) |
| GBF.MENU.FILE.QUIT | Save+Exit |  Ctrl+Q Alt+F4  |  Exit button on button bar X in top right hand corner  |
There are three possibilities for obj.id:
| | |
|---|---|
| obj.id < 0 |  More that one object was currently selected when this menu item was chosen and obj.id contains the negative number of selected objects, that is: -obj.id is the actual number of selected objects. So obj.id in this case is no valid object identification, but on the other hand object.key and object.value contain the identification of the first selected object. All currently selected objects can be obtained using a [gbf.get.selected()](gbf.get.selected.md) for each selected object. This case will only happen if the GBF is configured to support multiple select (see [gbf.init()](gbf.init.md))  |
| obj.id = 0 | No object was currently selected when this menu entry was chosen, and object.key will be an empty string, that is isspace(object.key) is true.  |
| obj.id > 0 | Precisely one object was currently selected when this menu item was chosen and that object is identified by obj.id as well as by the object.key and object.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call. The given obj.id identifies the object for the GBF and should be used only as object identification for other GBF functions like [gbf.get.parent()](gbf.get.parent.md), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and gbf.update.object().  |
After the saving is done the return value of this function to GBF uses the same return patterns as [gbf.menu.selected()](gbf.menu.selected.md). Note that even on GBF.MENU.FILE.QUIT the main application should still return to the GBF as the GBF will perform the exit part. This exit part may be skipped, that is the GBF will remain running when the special return value: GBF.DO.NOT.EXIT is returned in this case. This may be necessary when, for example, the user should have selected an object but they did not do so. The code in this case looks like:
```

function extern long gbf.save(…)
{
        if (save.type = GBF.MENU.FILE.QUIT) and (obj.id = 0) then
                | Please select at least one object before leaving
                mess("xxxxxxxxxx", 1)
                return (GBF.DO.NOT.EXIT)
        endif
        …
        return (0)
}
```

## Arguments
| | | |
|---|---|---|
| `long` | `obj.id` |  See above.  |
| `const string` | `object.key()` |   |
| `long` | `object.value` |   |
| `long` | `save.type` |   |

## Return values
See [gbf.menu.selected()](gbf.menu.selected.md)

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
