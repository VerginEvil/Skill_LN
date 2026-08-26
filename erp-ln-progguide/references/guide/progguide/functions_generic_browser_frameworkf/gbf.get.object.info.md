# gbf.get.object.info()

## Syntax:
`function long gbf.get.object.info( long object.id, ref string key(), ref string description(), ref long value, ref long type )`

## Description
This function returns the information of the object *obj.id*. The returned information is the information set at the call to [gbf.add.object()](gbf.add.object.md).

## Arguments
| | | |
|---|---|---|
| `long` | `object.id` |  The unique object identification.  |
| `ref string` | `key()` |  The key of the object by which it is known in the application.  |
| `ref string` | `description()` |  The text that is displayed in the browser to describe the object.  |
| `ref long` | `value` |  The value of the object that is used to further identify this object (in case the object appears more than once in the tree). Note that a value of 0 means something special, see [gbf.update.object() *](gbf.update.md).  |
| `ref long` | `type` |  Specify the object type by choosing one of the following: GBF.HEADER GBF.INTERIOR GBF.LEAF  |
-
-
-

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OBJECT | GBF is not in the right state to deal with this function  |

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
