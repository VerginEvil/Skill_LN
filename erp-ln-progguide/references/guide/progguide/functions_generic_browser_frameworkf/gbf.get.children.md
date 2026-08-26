# gbf.get.children()

## Syntax:
`#include <bic_gbf>`
`function long gbf.get.children( const string object.key(), long object.value, long cur.level )`

## Description
This function will be called by the GBF whenever it has the need for the children of a specific parent, for example after a parent is opened or after a refresh.
Note that the application may have defined other fetch child functions, instead of this function, see [gbf.set.child.function()](gbf.set.child.function.md) Still the GBF assumes that the interface (incoming arguments as well as the return values) are exactly the same as defined here.
Using functions like [gbf.get.first.child()](gbf.get.first.child.md) and [gbf.get.next()](gbf.get.next.md) is dangerous and should be avoided, especially when the force.read is set to TRUE, since that may lead to recursive calls towards this [gbf.get.children()](gbf.get.children.md) function.

## Arguments
| | | |
|---|---|---|
| `const string` | `object.key()` |  The parent is identified by the object.key and object.value, which have been given to the GBF on a preceding [gbf.add.object()](gbf.add.object.md) call. Note that in this particular call the obj.type argument must have been set to GBF.INTERIOR otherwise this function ( [gbf.get.children()](gbf.get.children.md)) would not have been called for this object.  |
| `long` | `object.value` |   |
| `long` | `cur.level` |  The cur.level indicates the current level of the given object. The level is defined as: 1 for every object which is added to the GBF by a [gbf.add.object()](gbf.add.object.md) call when called from a [gbf.get.top.level()](gbf.get.top.level.md) function call 1 + cur.level for each child which is added to the GBF with [gbf.add.object()](gbf.add.object.md) when called from this gbf.get.children() call.  |

## Return values
| | |
|---|---|
| GBF.DO.CONTINUE or 0 | Successful completion, GBF will continue working  |
| GBF.DO.ABORT | Abort GBF, which will end the GBF and return with an error, see [gbf.start()](gbf.start.md) |
| GBF.DO.EXIT | Finish GBF, which will end the GBF and return with 0, see [gbf.start()](gbf.start.md) |
Any return other than these values will be treated as if GBF.DO.ABORT has been returned

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
