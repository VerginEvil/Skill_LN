# form.text$()

## Syntax:
`function string form.text$( string messcode, [ string language_code ] )`

## Description
This retrieves a message from the data dictionary. It is used for constructing strings with parameter substitution. For messages to the screen, use [mess()](mess.md).

## Arguments
| | | |
|---|---|---|
| `string` | `messcode` |  The message code of the required message.  |
| `[ string` | `language_code ]` |  The language code. If you do not specify a language code, the user language is used. Otherwise the message with the specified language is retrieved (if available).  |

## Return values
The message string.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.

## Example
```

| Suppose there is a message code "pcgen00016" in the data
| dictionary with the text "Error %d in file %s".

string error(80)
error = form.text$("pcgen00016")        | error now contains
                                        | "Error %d in file %s"
error = sprintf$(error, e, filename$)   | error now contains, for
example
                                        | "Error 13 in file
tttmir001"
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
