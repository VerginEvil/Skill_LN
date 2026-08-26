# gbf.on.drop()

## Syntax:
`#include <bic_gbf>`
`function long gbf.on.drop( long from.pid, long collection, long drop.obj, const string drop.key, long drop.value, long drop.type, boolean copy )`

## Description
Call back function which is passed in function [gbf.enable.drop()](gbf.enable.drop.md) This function will be called when a drop event from the associated session arrives. In this function the business logic related to the drop operation must be implemented.

## Arguments
| | | |
|---|---|---|
| `long` | `from.pid` |  the process id of the session from which the objects are dropped  |
| `long` | `collection` |  collection of key fields objects which are dropped on this session  |
| `long` | `drop.obj` |  object identifier of GBF object on which the collection is dropped  |
| `const string` | `drop.key` |  GBF key related to drop.obj  |
| `long` | `drop.value` |  GBF value related to drop.obj  |
| `long` | `drop.type` |  GBF object type related to drop.obj  |
| `boolean` | `copy` |  when true, the user indicated that a copy operation is requested (CTRL key pressed during drop operation). Otherwise a move operation is required  |

## Return values
The return value is treated in the same way as with the [gbf.menu.selected()](gbf.menu.selected.md) function and it applies the drop object.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Composite Sessions overview](../functions_composite_sessions/overview.md)
- [Key fields Object overview](../functions_keyfields/overview.md)
