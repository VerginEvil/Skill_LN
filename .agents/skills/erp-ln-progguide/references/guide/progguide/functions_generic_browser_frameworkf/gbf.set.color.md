# gbf.set.color()

## Syntax:
`function long gbf.set.color( long color, const string color.desc() )`

## Description
Adds a description to the given color. This color.desc should be a message, which will be displayed when the Help on colors (Help -> Color Descriptions…) is activated. These colors are the colors with which the actual object have been added to the GBF. See the text.color argument of the [gbf.add.object()](gbf.add.object.md) function. When using the same color then only the last color.description of this color will be remembered, even when this color.description is empty when a preceding color.description was not empty.

## Arguments
| | | |
|---|---|---|
| `long` | `color` |  The color RGB value  |
| `const string` | `color.desc()` |  The description for this color  |

## Return values
| | |
|---|---|
| 0 | Success |
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
