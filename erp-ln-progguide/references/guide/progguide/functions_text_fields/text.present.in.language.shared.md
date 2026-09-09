# text.present.in.language.shared()

## Syntax:
`function long text.present.in.language.shared( string text_field, string lang, [ ref long nr_lines ] )`

## Description
This tests whether a specified text is available in a specified language. This function takes table sharing into account.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field which must be checked. See [Text fields overview](overview.md). If the specified text does not exist, nothing happens and the function returns 0.  |
| `string` | `lang` |  The language for which you wish to test the availability of the text.  |
| `[ ref long` | `nr_lines ]` |  This optional argument returns the number of lines the text occupies in the specified language.  |

## Return values
1 (true) text available in specified language
0 (false) text not available in specified language

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1920.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
