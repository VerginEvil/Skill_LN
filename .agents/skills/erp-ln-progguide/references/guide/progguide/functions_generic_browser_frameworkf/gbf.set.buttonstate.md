# gbf.set.buttonstate()

## Syntax:
`function long gbf.set.buttonstate( long button.id, long button.state )`

## Description
This function regulates the state of the standard buttons. This function can only be used if the default.button mask in the function [gbf.init()](gbf.init.md) is set with the standard buttons that need to be controlled. The old behavour of this option was that all the standard buttons were shown but disabled. This is still the case but now it is possible to enable or disable these buttons. When, however, the standard.button mask is used then it is not possible to adjust the standard buttons using this function. The GBF will then take over controll of these buttons. This is also default behavior. To improve the accessibility to the buttons the application function [gbf.on.selection()](gbf.on.selection.md) can be used. This function is called whenever a selection is made. It is clear that the user of this function is fully responsible for the behavior of the buttons. The following table gives the buttons that can be manipulated through this function:
| | |
|---|---|
| Button.id | Description |
| GBF.BUTTON.COPY | Copy the current selected object(s) |
| GBF.BUTTON.CUT | Cut (delete) the current selected object(s) |
| GBF.BUTTON.DELETE | Delete the current selected object(s) |
| GBF.BUTTON.GRP.NEW | Insert a new group object |
| GBF.BUTTON.INSERT | Insert a new object |
| GBF.BUTTON.PASTE | Paste the contents of the cut/copy buffers into the current selected object |
| GBF.BUTTON.TEXT | Start the text editor for the current selected object(s) |
| GBF.BUTTON.UNDO | Undo the last operation |

## Arguments
| | | |
|---|---|---|
| `long` | `button.id` |  The identification of the button. See the list above.  |
| `long` | `button.state` |  The state of the buttons or button.state can be either GBF.DISABLED or GBF.ENABLED.  |

## Return values
| | |
|---|---|
| 0 | Success |
| GBF.NO.BUTTON | The requested button does not exist |
| GBF.ILL.BUTTON | The given button is illegal or not supported yet |
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
