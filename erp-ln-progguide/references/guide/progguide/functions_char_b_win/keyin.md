# keyin$()

## Syntax:
`function string keyin$( [ long flag ] )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This reads the first character from the keyboard buffer. If there is no character in the buffer, the function waits until one is entered.
If you include the optional argument, the function performs a non-blocking read. If there is no character in the buffer, the function returns immediately with an empty string. This form of the function is used for interrupting a batch process when the user presses a key.
The function converts the following function keys to ASCII characters:
| | | | |
|---|---|---|---|
| Key | Ascii |  |  |
| <Arrow Left> | BS | 8 | ^H |
| <Arrow Right> | FF | 12 | ^L |
| <Arrow Up> | VT | 11 | ^K |
| <Arrow Down> | LF | 10 | ^J |
| <Insert> | EM | 25 | ^Y |

## Arguments
| | | |
|---|---|---|
| `[ long` | `flag ]` |    |

## Return values
The character read from the event queue. If the returned string contains multiple bytes, the character is a multibyte character. If the character is a function that cannot be converted, the function returns an empty string.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

repeat
  ...
until (keyin$(99)=chr$(27)) | until <Esc> is pressed
```
Note that the above example is very time consuming.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)

- [data.input()](data.input.md)

- [Events overview](../events/overview.md)
