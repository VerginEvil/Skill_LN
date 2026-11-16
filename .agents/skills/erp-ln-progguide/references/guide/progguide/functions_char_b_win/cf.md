# cf$()

## Syntax:
`function string cf$( long attribute_code )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to send a control code to the current window or printer. All characters after the command are printed or displayed in the font associated with the control code. To reset the font to normal, call `cf$(0)`.
The following codes are available:
| | | |
|---|---|---|
| Code | Screen | Printer |
| 0 | normal | normal |
| 1 | bold | bold |
| 2 | blinking | bold |
| 3 | bold blinking | bold |
| 4 | reverse | reverse |
| 5 | bold reverse | bold reverse |
| 6 | blinking reverse | bold reverse |
| 7 | bold blinking reverse | bold reverse |
| 8 | underscore | underscore |
| 9 | underscore bold | underscore bold |
| 10 | underscore blinking | underscore bold |
| 11 | underscore bold blinking | underscore bold |
| 12 | underscore reverse | underscore reverse |
| 13 | underscore reverse bold | underscore bold reverse |
| 14 | underscore reverse blinking | underscore bold reverse |
| 15 | underscore reverse bold blinking | underscore bold reverse |

## Arguments
| | | |
|---|---|---|
| `long` | `attribute_code` |    |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  If the printer is unable to print in reverse, text is printed in bold instead. Blinking is possible only on ASCII terminals.

## Example
```

| To screen
print cf$(4),"This is reversed printing on the screen",cf$(0)

| To printer
spool.pr.line = cf$(4)&"Printed reverse"&cf$(0)
spool.line()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
