# gbf.add.column()

## Syntax:
`function long gbf.add.column( const string column.name(), const string column.label() mb, [ boolean is.initially.hidden ] )`

## Description
Adds a Column to the Tree-Grid of a Tree-Detail session.

## Arguments
| | | |
|---|---|---|
| `const string` | `column.name()` |  The unique name of the Column  |
| `const string` | `column.label() mb` |  The text that is displayed above the Column, and in the Personalize Column option.  |
| `[ boolean` | `is.initially.hidden ]` |  Tells whether the Column is initially hidden. Default the column will be visible.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.STATE | GBF is not in the correct state to deal with this function. GBF is not part of a Tree-Detail session.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2230.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Restriction
This function may only be called by the application if the GBF is part of a Tree-Detail session.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)
- [Generic Browser Framework (GBF) synopsis](synopsis.md)
- [Typical usage](typical_usage.md)
- [Getting started](getting_started.md)
- [Example](example.md)
- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)
- [standard menu items and function keys](standard_menu_items_and_function_keys.md)
- [Messages and questions](messages_and_questions.md)
