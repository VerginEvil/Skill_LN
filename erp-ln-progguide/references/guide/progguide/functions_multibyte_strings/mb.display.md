# mb.display()

## Syntax:
`function long mb.display( string string_expr, ref string substr$, long space, [ long flags ] )`

## Description
This function returns that part of a specified string that fits in a specified display space. The substring is equal to the source string if the source string fits in the display space. If one or more characters do not fit in the display space, a ghost character (default is >) is appended to the substring.

## Arguments
| | |
|---|---|
| TSS_REVERSE | Reverse the substring if the current user environment is bidirectional and if `string_expr` contains bidirectional characters. The substring is ready for display. |
| TSS_FILLOUT | Fill the substring with trailing spaces, so that the width of the string equals the display space. This is the default if no flags are specified. |
| TSS_FORCE_REVERSE | Reverse the substring if `string_expr` contains bidirectional characters. The substring is ready for display. |
| TSS_FILTER_ESC | Filter out escape sequences. |
| TSS_FILTER_CF | Filter out code features. |

## Return values
An index to omitted characters if the string is truncated. Otherwise, the length of the string.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
