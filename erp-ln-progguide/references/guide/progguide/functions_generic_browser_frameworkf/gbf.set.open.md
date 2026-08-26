# gbf.set.open.strategy() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.open.strategy( long open.strategy )`
`function long gbf.set.open.child( long open.strategy )`
`function long gbf.set.open.read( long open.strategy )`
`function long gbf.set.open.what( long open.strategy )`

## Description
These functions set the open or close strategy, which is what the GBF should do when an interior node is closed and opened again as well as what should be done on the Open All menu item or Ctrl+O keystroke.

## gbf.set.open.child()
[gbf.set.open.child() *](gbf.set.open.child.md)

## gbf.set.open.read()
[gbf.set.open.read() *](gbf.set.open.read.md)

## gbf.set.open.what()
[gbf.set.open.what() *](gbf.set.open.what.md)

## gbf.set.open.strategy()
For the function [gbf.set.open.strategy() *](gbf.set.open.md) the open.strategy is a combination of these three. These option flags should be add (‘+’) or bit.or()’ed. The default of GBF for gbf.set.open.strategy() is:
GBF.OPEN.AGAIN + GBF.OPEN.NOREAD + GBF.OPEN.ALLTREE.
Take care when using gbf.set.open.strategy() in cases where only one or two of the open strategy parts has to be changed, since the other values should remain unchanged. This is in fact the reason why the other three functions are added. For example, when one wants to use the GBF.OPEN.READALL strategy the following code should be used:
```

function long force.open.read()
{
        long retval, strategy
        retval = gbf.get.open.strategy(strategy)
        if retval < 0 then      return (retval) endif
        strategy = GBF.OPEN.READALL +
        bit.and(strategy, bit.inv(GBF.OPEN.NOREAD + GBF.OPEN.READALL))
        return (gbf.set.open.strategy(strategy))
}
```

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

## gbf.set.open.child(), gbf.set.open.strategy(), gbf.set.open.read(), gbf.set.open.what()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
