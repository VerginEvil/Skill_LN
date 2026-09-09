# gbf.set.tree.report.subtitle()

## Syntax:
`function void gbf.set.tree.report.subtitle( const string sub.title(80) mb )`

## Description
This function can be used to set the subtitle for the ASCII print report. The default value for this variable, which represents a subtitle for this report, is
"(<session code> <session description>)"
The presence of the <session code> depends on the user settings.
By means of this function an alternate subtitle can be set for ASCII print reports. It should be called during the initialization phase of any session that uses the GBF tree functionality.

## Arguments
| | | |
|---|---|---|
| `const string` | `sub.title(80) mb` |  The subtitle for the ASCII print report.  |

## Return values
None

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
