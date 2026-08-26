# gbf.set.refresh.strategy()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.refresh.strategy( long refresh.rate, long refresh.type )`

## Description
Sets the automatic refresh rate and strategy, which means that after refresh.rate milliseconds the tree as maintained by GBF will be refreshed using the indicated strategy. A value of 0 for refresh.rate means no automatic refreshing and that refresh.type is ignored. The timing starts immediately after this function call when the GBF is already active, or immediately after the [gbf.start()](gbf.start.md) call.
The default of GBF is to have a refresh.rate of 0.

## Arguments
| | | |
|---|---|---|
| `long` | `refresh.rate` |  The number of milliseconds between refreshes. A value of 0 means no automatic refreshing and that the refresh.type may be ignored.  |
| `long` | `refresh.type` |  The refresh.type may be one of the following: GBR.REFRESH.ALL refresh the whole tree, including what is not open GBF.REFRESH.OPEN refresh only what is open, so when an interior node is closed, its child nodes will not be updated.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
|  GBF.ILL.REFRESH. RATE  | Illegal (negative) refresh.rate |
|  GBF.ILL.REFRESH. TYPE  | Unknown refresh.type specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

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
