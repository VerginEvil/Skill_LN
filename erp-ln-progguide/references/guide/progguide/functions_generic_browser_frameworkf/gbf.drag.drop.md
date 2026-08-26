# gbf.drag.drop()

## Syntax:
`#include <bic_gbf>`
`function long gbf.drag.drop( long drag.obj, const string drag.key(), long drag.value, long drag.type, long drop.obj, const string drop.key(), long drop.value, long drop.type, long button.mode )`

## Description
This function will be called by the GBF when a drag and drop operation has been performed by the end-user. Note that in order to receive these function calls, the GBF must be configured for drag and drop (see [gbf.init()](gbf.init.md)), otherwise it will not support drag and drop. Also when the GBF is not configured for multiple select, then always only one object can be dragged and dropped.
The *drag.obj* identifies the object(s) being dragged:
| | |
|---|---|
| drag.obj.< 0 |  More that one object was currently selected when the drop was done and drag.obj contains the negative number of selected objects, that is: -drag.obj is the actual number of selected objects. So drag.obj in this case is NO valid object identification, but on the other hand drag.key, drag.value and drag.type contain the identification of the first selected object. All currently selected objects can be obtained using a gbf.get.selected() This case will only happen if the GBF is configured to support multiple select (see [gbf.init()](gbf.init.md))  |
| drag.obj = 0 | Cannot happen |
| drag.obj > 0 | Precisely one object was selected when the drop was done and that object is identified by drag.obj as well as by the object.key and object.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call, that includes the drop.type, which indicates the type of drag.obj. The given drag.obj identifies the object for the GBF and should be used only as object identification for other GBF functions like [gbf.get.parent()](gbf.get.parent.md), [gbf.get.first.child()](gbf.get.first.child.md), [gbf.get.next()](gbf.get.next.md) and gbf.update.object().  |
The drop target, that is the object on which the selected objects are dropped, is identified by the drop.obj, drop.key, drop.value and drop.type, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call.
The GBF will prevent dragging and dropping on or off header objects. In other words drag.type and/or drop.type will never be GBF.HEADER.
Note that the application may have defined other fetch child functions, in stead of this function, see [gbf.set.child.function()](gbf.set.child.function.md). Still the GBF assumes that the interface (incoming arguments as well as the return values) are exactly the same as defined here.

## Arguments
| | | |
|---|---|---|
| `long` | `drag.obj` |  See above.  |
| `const string` | `drag.key()` |   |
| `long` | `drag.value` |   |
| `long` | `drag.type` |   |
| `long` | `drop.obj` |   |
| `const string` | `drop.key()` |   |
| `long` | `drop.value` |   |
| `long` | `drop.type` |   |
| `long` | `button.mode` |  The button.mode indicates which keys are hold down, possible values: EVTSHIFTMASK and/or EVTCONTROLMASK, indicating that the Shift key and/or Ctrl key are/were pushed down at the moment of the drop.  |

## Return values
The return value is treated in the same way as with the [gbf.menu.selected()](gbf.menu.selected.md) function call and it applies to both the dragged objects as well as to the drop object.

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
