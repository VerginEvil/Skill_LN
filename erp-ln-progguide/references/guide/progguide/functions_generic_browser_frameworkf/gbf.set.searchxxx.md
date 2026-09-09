# gbf.set.search.strategy() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.search.strategy( long search.strategy )`
`function long gbf.set.search.headers( long search.strategy )`
`function long gbf.set.search.sensitive( long search.strategy )`
`function long gbf.set.search.set( long search.strategy )`
`function long gbf.set.search.what( long search.strategy )`

## Description
The function gbf.set.search.strategy sets the search strategy, which means that starting with the next search, this strategy will be used.

## gbf.set.search.headers()
[gbf.set.search.headers() *](gbf.set.search.headers.md)

## gbf.set.search.sensitive()
[gbf.set.search.sensitive() *](gbf.set.search.sensitive.md)

## gbf.set.search.what()
[gbf.set.search.what() *](gbf.set.search.what.md)

## gbf.set.search.headers()
[gbf.set.search.headers() *](gbf.set.search.headers.md)

## gbf.set.search.strategy()
For the function gbf.set.search.strategy() the search.strategy is a combination of these three. These option flags should be add (‘+’) or bit.or()’ed. The default of GBF for gbf.set.search.strategy() is:
GBF.SEARCH.CURRENT + GBF.SEARCH.INSENSITIVE + GBF.SEARCH.DESCRIPTION + GBF.SEARCH.NO.HEADERS
Take care when using gbf.set.search.strategy() in cases where only one or two the search strategy parts has to be changed since the other values should remain unchanged. This is in fact the reason why the other three functions are added. For example when one wants to use the GBF.SEARCH.INSENSITIVE strategy the following code should be used:
```

function long force.search.insensitive()
{
        long retval, strategy
        retval = gbf.get.search.strategy(strategy)
        if retval < 0 then      return (retval) endif
        strategy = GBF.SEARCH.INSENSITIVE +
        bit.and(strategy, bit.inv(GBF.SEARCH.SENSITIVE + GBF.SEARCH.INSENSITIVE))
        return (gbf.set.search.strategy(strategy))
}
```
Note that when the search strategy is changed the submenu items under the search menu are also updated with the tic-mark showing the current search strategy (see [gbf.init()](gbf.init.md) menu options: GBF.MENU.SRCH.CURR, GBF.MENU.SRCH.READ and so on.).

## Arguments
| | | |
|---|---|---|
| `long` | `search.strategy` |  See above.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.SEARCH. TYPE | Unknown search strategy |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## gbf.set.search.headers(), gbf.set.search.sensitive(), gbf.set.search.set(), gbf.set.search.what()

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
