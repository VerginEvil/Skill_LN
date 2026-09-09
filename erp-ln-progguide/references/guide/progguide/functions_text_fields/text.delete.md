# text.delete()

## Syntax:
`function long text.delete( string text_field, string lang )`

## Description
This deletes a specified text.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field that must be deleted. See [Text fields overview](overview.md). This returns the text number of the field.  |
| `string` | `lang` |  The language for which the text must be deleted. To delete the text for all languages, specify an empty string here. In this case, the text number and all attributes of the text are deleted from the text manager. This also happens if the language you specify is the only language for which the text exists.  |

## Return values
> 0 success; returns the number of lines deleted
-1 error

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
