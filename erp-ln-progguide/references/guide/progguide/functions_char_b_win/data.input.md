# data.input()

## Syntax:
`function void data.input( string options(.), ref string result(.), string default(.), ref long event(EVTMAXSIZE), ref long char_value )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This reads data from the keyboard.
If the function specifies a default value, that value is displayed on screen. The value is accepted when the user presses ENTER. However, if the user enters a character at the first position in the field, the default value is deleted.
Normally, characters typed by the user are inserted before the current cursor position. However, if option 'C' is included in the *options* argument, characters typed by the user are inserted at the current cursor position.
Users can edit the default value or make minor corrections to the string entered (before they press ENTER) by using the following keys:
| | |
|---|---|
| RIGHT ARROW | Scroll right. |
| LEFT ARROW | Scroll left. |
| DEL | Delete character at cursor position. Characters to the right of the deleted character are moved one position to the left. If the cursor is positioned beyond the last character, this character is deleted and the cursor moves one position to the left. Pressing DEL in an empty field redisplays the default value.  |
| CTRL+X | Clear field. |
| TAB | Delete all characters from the cursor position to the end of the field.  |

## Arguments
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
```

            L='ABC\013^N^P\E\n\\'
```
| | | |
|---|---|---|
| `string` | `options(.)` |  This argument must either be empty or it must contain 5 parts separated by one or more spaces. If it is empty, the following input characteristics apply: no fill characters are displayed input starts at the current cursor position all characters are permitted the maximum number of characters that can be input is 132 If it is not empty, it must include the following five items: the starting column the starting row the minimum length of the string to be read the maximum length of the string to be read zero or more options The following options are available. You can specify them with or without separating spaces.  |
| `ref string` | `result(.)` |  This returns the value typed by the user. The argument must be declared as a one-dimensional string.  |
| `string` | `default(.)` |  A default string that is displayed on screen.  |
| `ref long` | `event(EVTMAXSIZE)` |  If the function is stopped as a result of an event, that event is stored in this argument. See [Events.](../events/overview.md)  |
| `ref long` | `char_value` |  If the function is stopped by input of a special character, the character typed is stored in this argument.  |

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
