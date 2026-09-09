# text.copy.language.shared()

## Syntax:
`function long text.copy.language.shared( string text_field, string lang_from, string lang_to )`

## Description
This copies a specified text from one language to another. This function takes table sharing into account.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field which must be copied. See [Text fields overview](overview.md). If the specified text does not exist, nothing happens and the function returns 0.  |
| `string` | `lang_from` |  This specifies the language from which the text must be copied.  |
| `string` | `lang_to` |  This specifies the language to which the text must be copied.  |

## Return values
> 0 success; returns the number of lines copied
0 error; text not found for source language
-1 error; switch to the company that stores the texts failed

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1920.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
