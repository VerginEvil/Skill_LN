# gbf.set.search.what() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.search.what( long search.strategy )`

## Description

## gbf.set.search.what()
The function gbf.set.search.what() defines what to search for. The search.strategy may be one of:
| | |
|---|---|
| GBF.SEARCH.DESCRIPTION | Search in the descriptions of the objects |
| GBR.SEARCH.KEY | Search in the codes (or keys) of the objects |

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
