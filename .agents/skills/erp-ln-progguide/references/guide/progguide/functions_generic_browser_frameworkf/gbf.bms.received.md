# gbf.bms.received()

## Syntax:
`#include <bic_gbf>`
`function long gbf.bms.received( long sender.id, const string mask(), const string mss(), long length )`

## Description
This function will be called by the GBF when the GBF receives a BMS message that it cannot handle itself. The application should now deal (or ignore) this message.
Note
The nature of these BMS messages is that they arrive at undeterminable times, so one should not assume that the message is related to the current selected object(s), so be very careful with actions or return values such as delete current selected object.

## Arguments
| | | |
|---|---|---|
| `long` | `sender.id` |  The Baan process which has send this message.  |
| `const string` | `mask()` |  The mask with which the message has been send  |
| `const string` | `mss()` |  The actual BMS message  |
| `long` | `length` |  The length of the message mss  |

## Return values
The return value is treated in the same way as with the [gbf.menu.selected()](gbf.menu.selected.md) function call, but be very careful with operations on the current selected object.

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
