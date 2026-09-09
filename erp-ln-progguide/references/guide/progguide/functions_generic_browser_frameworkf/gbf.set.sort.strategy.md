# gbf.set.sort.strategy()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.sort.strategy( long sort.strategy )`

## Description
This function sets the automatic sort strategy, which tells the GBF how to sort the child nodes of an interior node. The sort.strategy is the same for the whole tree, that is it is not possible to define different sort strategies for different interior nodes. If this is really wanted, then the application should be doing the sorting.
sort.strategy
The sort.strategy may be one of:
| | |
|---|---|
| GBR.SORT.NONE | GBF does not sort itself, it uses the order in which the nodes are handed over |
| GBF.SORT.DESC | GBF will sort the nodes using the description |
| GBF.SORT.KEY | GBF will sort the node using the key |
Apart from the item to be sorted on, also the sort order can be chosen. These options should be added to the sort.strategy. Possible values are:
| | |
|---|---|
| GBF.SORT. ASCENDING | Ascending sorting |
| GBF.SORT. DESCENDING | Descending sorting |
Finally you can also choose whether or not case insensitive sorting should be done. These options should be added to the sort strategy. Possible values are:
| | |
|---|---|
| GBF.SORT.SENSITIVE | Make distinction between lower and upper case |
| GBF.SORT. INSENSITIVE | Make no distinction between lower and upper case |
The default sort strategy of GBF is GBF.SORT.NONE.

## Arguments
| | | |
|---|---|---|
| `long` | `sort.strategy` |  See above.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.SORT.TYPE | Unknown sort strategy specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

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
