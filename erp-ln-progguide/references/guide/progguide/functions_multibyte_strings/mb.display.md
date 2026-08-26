# mb.display()

## Syntax:
`function long mb.display( string string_expr, ref string substr$, long space, [ long flags ] )`

## Description
This function returns that part of a specified string that fits in a specified display space. The substring is equal to the source string if the source string fits in the display space. If one or more characters do not fit in the display space, a ghost character (default is >) is appended to the substring.

## Arguments
| | | |
|---|---|---|
| `string` | `string_expr` |  The source string.  |
| `ref string` | `substr$` |  The returned substring. This ends with a ghost character if some characters of the source string do not fit in the specified display space.  |
| `long` | `space` |  The size of the display space for the substring.  |
| `[ long` | `flags ]` |  These optional flags specify certain criteria for handling the substring. They are particularly useful for working with bidirectional strings.  |

## Return values
An index to omitted characters if the string is truncated. Otherwise, the length of the string.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
