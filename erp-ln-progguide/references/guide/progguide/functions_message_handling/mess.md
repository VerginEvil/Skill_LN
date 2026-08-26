# mess()

## Syntax:
`function void mess( string messcode, long separate_window, [ void arg ... ] )`

## Description
This retrieves a message from the data dictionary and displays it on screen. Using this function makes your program script language independent.

## Arguments
| | | |
|---|---|---|
| `string` | `messcode` |  The message code (including the package code). The language code of the user is automatically added. Both the message code and the user language must be available in the data dictionary.  |
| `long` | `separate_window` |  This specifies how the message can be removed:  |
| `[ void` | `arg ... ]` |  The message string in the data dictionary can contain format characters for parameter substitution. The values which must be substituted are specified in the 3rd, 4th, ... arguments of the function. The number of these arguments is variable.  |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  In 3GL scripts when *separate_window* is 1, the variable *graphical.mode* must be set to 1 if you want the message to be displayed in a separate window.

## Example
```

| Suppose there is a message code "pcgen00016" in the data
| dictionary with the text "Error %d in file %s"

mess("pcgen00016",1,e,filename$)   | Prompt for ENTER
mess("pcgen00016",0,e,filename$)   | Display message and continue
                                   | (if there is a current form)
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
