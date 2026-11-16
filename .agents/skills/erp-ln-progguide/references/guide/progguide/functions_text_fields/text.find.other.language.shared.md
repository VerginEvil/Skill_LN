# text.find.other.language.shared()

## Syntax:
`function string text.find.other.language.shared( string text_field )`

## Description
This function returns the language in which the most recent version of the text is stored. This function takes table sharing into account.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field which must be checked. See [Text fields overview](overview.md). If the specified text does not exist, nothing happens and the function returns 0.  |

## Return values
The language in which the text is last stored.
An empty string is returned in case of an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1920.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
