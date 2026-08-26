# gbf.set.open.depth()

## Syntax:
`function long gbf.set.open.depth( long open.depth )`

## Description
Sets the current open and read depth.

## Arguments
| | | |
|---|---|---|
| `long` | `open.depth` |  The number of levels the GBF will display when opening an interior node (double click on interior node or select one and press ENTER etc). When not all these levels have been read yet, the GBF will read the necessary levels. The default value for open.depth is 1. The special mnemonic GBF.READ.ALL can be used to identify that all available levels are read and opened, that is all the way down to either a cycle has been detected or a leaf node has been reached.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.LEVEL | Open.depth is not a valid number of levels: < 0  |
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
