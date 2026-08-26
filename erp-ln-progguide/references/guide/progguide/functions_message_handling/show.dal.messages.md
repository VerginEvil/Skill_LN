# show.dal.messages()

## Syntax:
`function void show.dal.messages( [ long i.type ] )`

## Description
Displays messages that are currently on the DAL message stack. Depending on the specified message type, you can display error, warning or info messages, or all messages. If no message type is specified, only error messages will be displayed.

## Arguments
| | | |
|---|---|---|
| `[ long` | `i.type ]` |  A message type. If not specified, only error messages are displayed. Parameter i.type should be one of the following values: MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Notes
The presentation of these messages depends on:
- the specified Message Type, one of `MSG.ALL, MSG.ERROR, MSG.WARNING, MSG.INFO`.
- the Message Mode setting of the user - Interactive or Non-interrupting (this can be set in the User Data session)

## Modal Dialog
In Interactive Mode when message type `MSG.ERROR` is specified, or no message type is specified at all, DAL messages are presented in a modal dialog. In this way the user is forced to take notice of the messages as the application will be blocked until the dialog closes.
The most recent (ie. the last added) message is shown at the top of the Error dialog. Any subsequent message is displayed on a separate line, prefixed by the word Reason, like this (example):

## Modeless Window
In Non-Interrupting mode, but also when `MSG.ALL`, `MSG.WARNING` or `MSG.INFO` is specified, all messages are displayed in a separate modeless window. Each message is displayed on a new line.

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
