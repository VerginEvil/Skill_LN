# mess()

## Syntax:
`function void mess( string messcode, long separate_window, [ void arg... ] )`

## Description
This retrieves a message from the data dictionary and displays it on screen. Using this function makes your program script language independent.

## Arguments
| | |
|---|---|
| 1 | The message is displayed in a separate window and the user must click a button in that window to remove the message. In job mode the message is logged in the job history. |
| 0 | The message is displayed on the status bar. The user cannot remove the message. It remains until removed by the [clean.mess()](clean.mess.md) function. In job mode the message is not logged in the job history. |

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  In 3GL scripts when *separate_window* is 1, the variable *graphical.mode* must be set to 1 if you want the message to be displayed in a separate window.

## Example
```

| Suppose there is a message code "pcgen00016" in the data
| dictionary with the text "Error %d in file %s"

mess("pcgen00016",1,e,filename$)   | Prompt for <Enter>
mess("pcgen00016",0,e,filename$)   | Display message and continue
                                   | (if there is a current form)
```

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
