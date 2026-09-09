# mb.isbidi.language()

## Syntax:
`function boolean mb.isbidi.language( string lang )`

## Description
This function checks whether the specified language is a bidirectional one. To use the function, you must link to the ttdllbidi library. The function checks the flag ‘ %TF@ttaad110.bidi’ in the table ‘%TB@ttaad110’.

## Arguments
| | | |
|---|---|---|
| `string` | `lang` |    |

## Return values
TRUE current language is bidirectional
FALSE current language is not bidirectional

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Multibyte strings overview and synopsis](overview_and_synopsis.md)
