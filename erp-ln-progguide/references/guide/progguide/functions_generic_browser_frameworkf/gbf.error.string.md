# gbf.error.string()

## Syntax:
`function string gbf.error.string( long error )`

## Description
Returns the string which represents the given error. This error should be a return value from any other GBF function call. This function translates such an (error) return value into its defined format.
For example:
sprintf$(“The error is: %s.”, gbf.error.string(GBF.NO.MEMORY))
will build the following string:
The error is: GBF.NO.MEMORY.

## Arguments
| | | |
|---|---|---|
| `long` | `error` |  The error return value.  |

## Return values
String holding the mnemonic value (or define).

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
