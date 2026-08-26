# mb.scrpos()

## Syntax:
`function long mb.scrpos( string string_value$, long string_position )`

## Description
This function converts a string position to a screen position. Escape sequences and code features are ignored.

## Arguments
| | | |
|---|---|---|
| `string` | `string_value$` |  The string value for which the string position must be converted to a screen position. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS.  |
| `long` | `string_position` |  The string position to be converted to a screen position. This is the 1-based index of a character in the supplied string value (converted to type multibyte string).  |

## Return values
| | |
|---|---|
| >= 1 |  The 1-based screen position corresponding to the supplied string position. The returned screen position is the 1-based index of a cell of the area in which the string value might be displayed. The cell specified by the returned screen position is the cell in which the character specified by the supplied string position might be displayed. If the specified character is a double-width character, then the returned screen position specifies the first of the two cells in which the character might be displayed. If the specified character is a zero-width character, then the returned screen position specifies the cell in which the character might be displayed if it were a single-width character. In all cases, the returned screen position is 1 greater than the display width of the substring before the specified character. Escape sequences and code features in the string value do occupy string positions, but are considered as having display width 0.  |
| -1 | When the supplied string position is less than 1, i.e. when it is 0 or negative. This is well specified behavior as of [porting set TIV](../tiv/tiv_overview.md) [level 2440](../tiv/tiv_2440.md). For earlier versions, the value returned for supplied string position less than 1 is left unspecified.  |
| -1 | When the supplied string position is greater than the character count of the supplied string value. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
The following example shows the relations between the string contents, the string positions, and the screen positions.
The example string contains:
- some single-width characters, chosen from the Latin script: A B C D ;
- some double-width characters, chosen from the Korean script: 가 각 갂 갃 ;
- some zero-width characters, represented by the symbol ↮ ;
- some spaces, represented by the symbol ␣ .  The full example string is `"AB↮CD가각↮↮갂갃␣↮␣␣"`.
Notice that this is the same string as used in the example section of the inverse operation [mb.strpos()](mb.strpos.md).
The first table shows the characters in the string.
| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Character position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Character | A | B | ↮ | C | D | 가 | 각 | ↮ | ↮ | 갂 | 갃 | ␣ | ↮ | ␣ | ␣ |
| Character display width | 1 | 1 | 0 | 1 | 1 | 2 | 2 | 0 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| Accumulated display width before character | 0 | 1 | 2 | 2 | 3 | 4 | 6 | 8 | 8 | 8 | 10 | 12 | 13 | 13 | 14 |
| Screen position | 1 | 2 | 3 | 3 | 4 | 5 (and 6) | 7 (and 8) | 9 | 9 | 9 (and 10) | 11 (and 12) | 13 | 14 | 14 | 15 |
The second table shows the characters on the screen.
| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Screen position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Character | A | B | ↮C | D | 가 | 각 | ↮↮갂 | 갃 | ␣ | ↮␣ | ␣ |  |  |  |  |
| Character position | 1 | 2 | 3, 4 | 5 | 6 | 7 | 8, 9, 10 | 11 | 12 | 13, 14 | 15 |  |  |  |  |

## Related topics
- Inverse operation: [mb.strpos()](mb.strpos.md)
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
