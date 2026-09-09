# gbf.on.drag()

## Syntax:
`#include <bic_gbf>`
`function long gbf.on.drag( long to.pid, const string to.session, long drag.obj, const string drag.key, long drag.value, long drag.type, reference long collection )`

## Description
This function will be called by the GBF when one or more GBF objects are dragged from this session and dropped on another composite child session. This function will only be called when dragging to other sessions is enabled (see [gbf.init()](gbf.init.md) default.options, *GBF.OPT.SESSION.DRAG*).
This callback function is supposed to create one or more key field objects related to the currently selected GBF objects and return this to the GBF framework through argument *collection*.

## Arguments
| | | |
|---|---|---|
| `long` | `to.pid` |  the process id of the session on which the GBF objects are dropped  |
| `const string` | `to.session` |  the code of the session on which the GBF objects are dropped  |
| `long` | `drag.obj` |  See the meaning of the argument *drag.obj* in the function description of [gbf.drag.drop()](gbf.drag.drop.md)  |
| `const string` | `drag.key` |  GBF key related to drag.obj  |
| `long` | `drag.value` |  GBF value related to drag.obj  |
| `long` | `drag.type` |  GBF object type to drag.obj  |
| `reference long` | `collection` |  This function is responsible for creating a collection of key field objects which are dragged from this session. The id of the created collection must be set in the collection argument. The GBF framework will make sure this collection is deleted when it is not needed anymore.  |

## Return values
| | |
|---|---|
| GBF.DO.CONTINUE | To indicate to the GBF framework that the drag/drop operation should continue with the passed key fields collection. |
| GBF.DO.ABORT | To indicate to the GBF framework that the drag/drop operation should be aborted. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Composite Sessions overview](../functions_composite_sessions/overview.md)

- [Key fields Object overview](../functions_keyfields/overview.md)
