# text.copy.language()

## Syntax:
`function long text.copy.language( long textnr, string lang_from, string lang_to )`

## Description
*Deprecated.* This function doesn't support shared tables and its usage is therefore deprecated. Use [text.copy.language.shared()](text.copy.language.shared.md) instead.
This copies a specified text from one language to another.

## Arguments
| | | |
|---|---|---|
| `long` | `textnr` |  The text number of the text that must be copied.  |
| `string` | `lang_from` |  This specifies the language from which the text must be copied.  |
| `string` | `lang_to` |  This specifies the language to which the text must be copied.  |

## Return values
> 0 success; returns the number of lines copied
0 error; text not found for source language

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
