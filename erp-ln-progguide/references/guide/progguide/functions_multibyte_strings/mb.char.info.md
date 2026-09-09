# mb.char.info()

## Syntax:
`function long mb.char.info( string tss_string$ )`

## Description
This function identifies the character set to which a [TSS-encoded](../misc/tss.md) character belongs. It returns the character set ID for the first character in the specified string.
In TSS, due to the phenomenon of unification, it is not in all cases clear to which character set a character belongs. This function tries all available character sets in a certain order and returns the ID of the first encountered character set containing a character that reasonably might have been mapped to the first character of the supplied string.

## Arguments
| | | |
|---|---|---|
| `string` | `tss_string$` |  The first character of the string will be used. It is not relevant whether the type of the string is single-byte string or multibyte string. The byte sequence in the string is interpreted as TSS, i.e. when the first byte has hexadecimal value 0x9b, then it is interpreted as the lead byte of a four-byte TSS sequence, encoding a single character.  |

## Return values
The ID of the character set for the first character in the specified string. Or -1 if *ch$* is an empty string or if the TSS character could not be found in one of the TSS character sets.
For the same character, different calls of this function can give different results. The search order is not the same for every call of mb.char.info. The character set resulting from a successful call of mb.char.info occurs early in the search order of the next call of mb.char.info. Also the character set of the current locale occurs early in the search order of each call.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [TSS Encoding](../misc/tss.md)

- [mb.locale.enumerate()](mb.locale.enumerate.md)

- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
