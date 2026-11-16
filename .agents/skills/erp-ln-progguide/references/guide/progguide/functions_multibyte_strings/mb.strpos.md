# mb.strpos()

## Syntax:
`function long mb.strpos( string string_value$, long screen_position )`

## Description
This function converts a screen position to a string position. Escape sequences and code features are ignored.

## Arguments
| | | |
|---|---|---|
| `string` | `string_value$` |  The string value for which the screen position must be converted to a string position. For the purpose of this function, the value is assumed to be [space padded](../3gl_features/fixed_and_based_variables.md) as far as its containing variable allows. Its contents, whether or not of type multibyte string, are considered to be encoded in TSS.  |
| `long` | `screen_position` |  The screen position to be converted to a string position. This is the 1-based index of a cell of the area in which the space padded string value might be displayed.  |

## Return values
| | |
|---|---|
| >= 1 | The 1-based string position corresponding to the supplied screen position. The returned string position should be interpreted as a 1-based character index, specifying the start position in the supplied string value ( [space padded](../3gl_features/fixed_and_based_variables.md) as far as its containing variable allows and converted to type multibyte string). In other words: when `fixed_mb_string$` is a sufficiently large [fixed (i.e. space padded)](../3gl_features/fixed_and_based_variables.md) [multibyte string variable](../3gl_features/multibyte_strings.md), and the supplied string value is assigned to it, then `fixed_mb_string$( string_position; 1 )` is the character displayed at the cell specified by the supplied screen position. The display width of the substring before the specified character (i.e. `fixed_mb_string$( 1; string_position - 1 )`) is 1 or 2 less than the supplied screen position. The display width of the substring up to and including the specified character (i.e. `fixed_mb_string$( 1; string_position )`) is equal to or 1 greater than the supplied screen position. Escape sequences and code features in the string value do occupy string positions, but are considered as having display width 0. |
| -1 | When the supplied screen position is less than 1, i.e. when it is 0 or negative. This is well specified behavior as of [porting set TIV](../tiv/tiv_overview.md) [level 2440](../tiv/tiv_2440.md). For earlier versions, the value returned for supplied screen position less than 1 is left unspecified. |
| -1 | When the supplied screen position is greater than the display width of the supplied string value (space padded as far as its containing variable allows). |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
The following example shows the relations between the string contents, the string positions, and the screen positions.
The example string contains:

- some single-width characters, chosen from the Latin script: A B C D;

- some double-width characters, chosen from the Korean script: 가 각 갂 갃;

- some zero-width characters, represented by the symbol ↮;

- some spaces, represented by the symbol ␣.

The full example string is `"AB↮CD가각↮↮갂갃␣↮␣␣"`.
Notice that this is the same string as used in the example section of the inverse operation [mb.scrpos()](mb.scrpos.md).
The first table shows the characters in the string.
| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Character position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Character | A | B | ↮ | C | D | 가 | 각 | ↮ | ↮ | 갂 | 갃 | ␣ | ↮ | ␣ | ␣ |
| Character display width | 1 | 1 | 0 | 1 | 1 | 2 | 2 | 0 | 0 | 2 | 2 | 1 | 0 | 1 | 1 |
| Accumulated display width | 1 | 2 | 2 | 3 | 4 | 6 | 8 | 8 | 8 | 10 | 12 | 13 | 13 | 14 | 15 |
| Screen position | 1 | 2 |  | 3 | 4 | 5, 6 | 7, 8 |  |  | 9, 10 | 11, 12 | 13 |  | 14 | 15 |
The second table shows the characters on the screen.
| | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Screen position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Character | A | B | C | D | 가 | 각 | 갂 | 갃 | ␣ | ␣ | ␣ |  |  |  |  |
| Character position | 1 | 2 | 4 | 5 | 6 | 7 | 10 | 11 | 12 | 14 | 15 |  |  |  |  |
| Accumulated display width before character | 0 | 1 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 13 | 14 |  |  |  |  |
| Accumulated display width including character | 1 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 13 | 14 | 15 |  |  |  |  |

## Related topics
- [mb.scrpos()](mb.scrpos.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
