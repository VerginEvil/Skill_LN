# mb.width()

## Syntax:
`function long mb.width( string string_value$ )`

## Description
This function returns the display width of the specified string; that is, the number of positions the string will occupy on the screen.

## Arguments
| | | |
|---|---|---|
| `string` | `string_value$` |  The string value of which the display width must be determined. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS.  |

## Return values
The display width of the specified string value.
A single-byte character has a display width of 0 or 1 screen positions. A multibyte character has a display width of 0 or 1 or 2 screen positions.
Escape sequences and code features in the string value are recognized and are considered as having display width 0.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
