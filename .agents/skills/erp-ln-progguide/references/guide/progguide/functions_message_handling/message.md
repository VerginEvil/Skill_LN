# message()

## Syntax:
`function void message( string mess_str, [ void arg... ] )`

## Description
This displays the specified message string on screen in a separate window, and waits until the user closes it. This is applicable in case the message mode of the concerning user is set to "Interactive". In case of a "Non-interrupting" message mode, Infor Enterprise Server displays the message strings in a separate "Messages" window without interruption.

## Arguments
| | | |
|---|---|---|
| `string` | `mess_str` |  The message string to be displayed. This can contain format characters for parameter substitution. For details about formatting a string see the [sprintf$()](../functions_formatting_io/sprintf.md).  |
| `[ void` | `arg... ]` |  The message string can contain format characters for parameter substitution. The values which must be substituted are specified in the 2nd, 3rd,... arguments of the function. The number of these arguments is variable.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Using *message()* makes your program script language dependent. If you require language independency, use [mess()](mess.md) instead.

## Example
```

| Suppose the user enters a non-existent code 123 (from
| pctst999.item) and you want to display the message:
| "Code (123) not found."

message("Code (123) not found.")

| However it is better to use parameter substitution:
message("Code (%d) not found.", pctst999.item)

| The following construction gives the message "Error 13 in file
| tpctst999", for example:

message("Error %d in file %s", e, filename$)
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
