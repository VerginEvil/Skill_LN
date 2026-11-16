# gbf.set.open.read() *

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.open.read( long open.strategy )`

## Description

## gbf.set.open.read()
The function gbf.set.open.read() deals with the Open All (Ctrl+O) menu item (keystroke) action. It determines what should be done on this action. The open.strategy in this case may be one of:
| | |
|---|---|
| GBF.OPEN.NOREAD | Open only what is already known to the GBF. In other words use only that what has already been read before. |
| GBF.OPEN.READALL | First performs a read all (that is: menu item: Read All or keystroke Ctrl+R) and then open all nodes. |

## Arguments
| | | |
|---|---|---|
| `long` | `open.strategy` |  See above.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.OPEN.TYPE | Unknown open.strategy specified |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

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
