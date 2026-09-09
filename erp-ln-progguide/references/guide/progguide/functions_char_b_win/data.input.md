# data.input()

## Syntax:
`function void data.input( string options(.), ref string result(.), string default(.), ref long event(EVTMAXSIZE), ref long char_value )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This reads data from the keyboard.
If the function specifies a default value, that value is displayed on screen. The value is accepted when the user presses <Enter>. However, if the user enters a character at the first position in the field, the default value is deleted.
Normally, characters typed by the user are inserted before the current cursor position. However, if option 'C' is included in the *options* argument, characters typed by the user are inserted at the current cursor position.
Users can edit the default value or make minor corrections to the string entered (before they press <Enter>) by using the following keys:
| | |
|---|---|
| <Arrow Right> | Scroll right. |
| <Arrow Left> | Scroll left. |
| <Del> | Delete character at cursor position. Characters to the right of the deleted character are moved one position to the left. If the cursor is positioned beyond the last character, this character is deleted and the cursor moves one position to the left. Pressing <Del> in an empty field redisplays the default value. |
| <Ctrl>+X | Clear field. |
| <Tab> | Delete all characters from the cursor position to the end of the field. |

## Arguments
```

            L='ABC\013^N^P\E\n\\'
```
| | |
|---|---|
| +ABIDI | Supports input of bidirectional data. |
| B | Empty result not permitted. |
| C | Overwrite mode. |
| E | E and e permitted as input; always converted to capital letter. |
| F | Effect of '.' (moving cursor to previous field) is switched off. |
| FILL='.' | The specified character is used as the fill character for the field. By default, the fill character defined for the user is used. |
| G | A floating-point number is expected. |
| K | Converts all uppercase characters to lower case. |
| L='..' | Characters specified by this option are interpreted as the end of input. When the user enters one of these characters, *data.input()* returns immediately without waiting for the user to press <Enter>. The *char_value* argument returns the decimal value of the character that was typed. You can specify any combination of the following characters with this option: ASCII characters A - Z, a - z, and others such as % & ! ?. Octal representation of characters; these must start with '\0'. For example: \01 and \012. Decimal representation of characters; these must start '\'. For example: \1 and \12. Hexadecimal representation of characters; these must start with '\0x'. For example: \0x1and \0x12. Control characters. For example: ^B and ^F. Backslash (\\). Circumflex (\^). Escape (\E or \e). Space (\s). New line,(\n). Return (\r). Form feed (\f). Previous line (\v). Backspace (\b). The following example specifies the following characters: A, B, C, octal 13, <Ctrl>+N, <Ctrl>+P, <Esc>, new line, and backslash. |
| LEN='..' | This specifies the available space on the terminal screen. If the cursor is at the beginning or end of the available space, the field scrolls horizontally. |
| N | An integer number is expected. |
| P | Entered characters are suppressed. No default value or fill characters are displayed on screen. |
| R | An automatic carriage return is executed when the last character is entered (that is, when the string is full). |
| T='..' | A string specifying all valid input characters. All other characters are invalid. |
| U | Converts all lowercase characters to uppercase. |
| V='..' | A string specifying all invalid characters. All other characters are valid. |
| Y | Result must be 'Y' or 'N'. Lowercase characters are converted to uppercase, so 'y' and 'n' are also permitted. If these characters are not specified with T='YyNn', other characters are also permitted. But after the user presses <Enter>, the message 'Only Y/N allowed' is displayed. |
| > | After the user presses <Enter>, the input string is right justified. |
| < | After the user presses <Enter>, the input string is left justified. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

string result(1)
data.input("0 0 1 1 UE T='YN'", result, "")
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)

- [keyin$()](keyin.md)
