# gbf.set.open.child() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.open.child( long open.strategy )`

## Description

## gbf.set.open.child()
The function gbf.set.open.child() deals with what to do with the children when reopening an interior node. The open.strategy in this case may be one of:
| | |
|---|---|
| GBF.OPEN.AGAIN | Open again all interior nodes which were already open when the original interior node was closed. That is restore the full state after a close - reopen sequence.  |
| GBF.OPEN.NONE | Do not open the interior nodes when reopening the original interior node, that is closes all these sub nodes.  |
| GBF.OPEN.REFRESH | Delete all nodes beneath the given node, which implies that when reopening this node its children will be read again.  |
The default of GBF is to have the open.type set to GBF.OPEN.AGAIN.
This open and close strategy is determined at the moment when the interior node gets closed (double click on open interior node and so on.). So when closing such a node, changing the open strategy and reopening that same interior node will reveal the contents of that node using the previous strategy and not the current strategy.

## Arguments
| | | |
|---|---|---|
| `long` | `open.strategy` |  See above.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OPEN.TYPE | Unknown open.strategy specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## gbf.set.open.child(), gbf.set.open.read(), gbf.set.open.strategy(), gbf.set.open.what()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
