# gbf.get.cutcopy()

## Syntax:
`function long gbf.get.cutcopy( long index, ref string obj.key(), ref string obj.description(), ref long obj.value )`

## Description
This function must only be used when a call back to the main application indicates that there are one or more objects in the cut, copy and paste buffers (see gbf.get.cutcopynr()). A further use of this function is immediately after the GBF has stopped (in other words the [gbf.start()](gbf.start.md) function call has completed) to get the current cut or copy objects, so in this case the GBF can be used as a zoom session to pick a specific object. This function then allows you to retrieve all the cut or copy objects one by one as it returns the cut or copy object at the given index. The object is identified by the obj.key, obj.desc and obj.value, which have been given to the GBF on a [gbf.add.object()](gbf.add.object.md) call.
Note that the internal GBF obj.id is not returned, since the object may no longer be present in the GBF, for example typically after the cut operation.
In case the application does not support multiple selection, this gbf.get.cutcopy() function can only be called with index set to 1.

## Arguments
| | | |
|---|---|---|
| `long` | `index` |  The index in the cut, copy and paste buffer. To retrieve the number of objects within the buffer, use the [gbf.get.cutcopy.nr()](gbf.get.cutcopy.nr.md) function.  |
| `ref string` | `obj.key()` |  A reference to the key of the object by which it is known in the application.  |
| `ref string` | `obj.description()` |  A reference to the text that is displayed in the browser to describe the object.  |
| `ref long` | `obj.value` |  A reference to the value of the object that is used to further identify this object (in case the object is in the tree more than once). Note that a value of 0 means something special, see gbf.update.object().  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OBJECT | Illegal index given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [gbf.get.cutcopy.nr()](gbf.get.cutcopy.nr.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
