# gbf.desc.to.column()

## Syntax:
`function string gbf.desc.to.column( const string column1, const string ... )`

## Description
Create a special description string which is used to separate columns.
The resulting string can be passed as the argument "object.description" to the functions gbf.add.header(), gbf.add.interior(), gbf.add.leaf() and gbf.add.object().

## Arguments
| | | |
|---|---|---|
| `const string` | `column1` |  The column 1 part of the description.  |
| `const string` | `...` |  Optional arguments containing the column 2, column 3 etc. parts of the description.  |

## Return values
A description string, containing the concatenated column descriptions, separated by a special separator character.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Restriction
Incase of BW/Worktop, this function requires that the option "GBF.OPT.FONT.FIXED" is passed to the gbf.init() function. Otherwise columns are not correctly alligned.

## Related topics
- [gbf.add.interior()](gbf.add.interior.md)
- [gbf.add.leaf()](gbf.add.leaf.md)
- [gbf.add.object()](gbf.add.object.md)
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
