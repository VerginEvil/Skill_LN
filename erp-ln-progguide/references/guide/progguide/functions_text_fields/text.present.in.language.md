# text.present.in.language()

## Syntax:
`function long text.present.in.language( long textnr, string lang, [ ref long nr_lines ] )`

## Description
*Deprecated.* This function doesn't support shared tables and its usage is therefore deprecated. Use [text.present.in.language.shared()](text.present.in.language.shared.md) instead.
This tests whether a specified text is available in a specified language.

## Arguments
| | | |
|---|---|---|
| `long` | `textnr` |  The text number of the relevant text.  |
| `string` | `lang` |  The language for which you wish to test the availability of the text.  |
| `[ ref long` | `nr_lines ]` |  This optional argument returns the number of lines the text occupies in the specified language.  |

## Return values
1 (true) text available in specified language
0 (false) text not available in specified language

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
