# gbf.enable.drop()

## Syntax:
`function long gbf.enable.drop( const string session.code, const string dllname, const string gbf.on.drop )`

## Description
Allow drop operation from objects dragged from the indicated composite child sessions. When an object from the indicated session is dropped, the function passed in parameter *gbf.on.drop* will be called. This function must be called by the application after [gbf.init()](gbf.init.md) has been called but before [gbf.start()](gbf.start.md) is called.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  code of the session from which objects can be dropped  |
| `const string` | `dllname` |  The name of the DLL in which the function *gbf.on.drop* is implemented. Usually you can use the return value of [gbf.current.library()](gbf.current.library.md)  |
| `const string` | `gbf.on.drop` |  The name of the function that will be called when a drop event occurs. This function must be declared as described here: [gbf.on.drop()](gbf.on.drop.md).  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.DLL | Illegal or unknown *dllname* specified  |
| GBF.ILL.FUNCTION | Illegal or unknown *gbf.on.drop* function specified  |
| GBF.ILL.STATE | GBF is not in the right state to handle this function |
| GBF.NO.MEMORY | not enough memory |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Composite Sessions overview](../functions_composite_sessions/overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
