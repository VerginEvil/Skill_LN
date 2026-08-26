# textfield.to.database()

## Syntax:
`function long textfield.to.database( string text_field )`

## Description
Gets the text from the text part of the specified field, and writes it into the texttable. If the text does not exist yet in the texttable, a new texttable record is created. This is only relevant for multiline text formfields in a non-maintable session.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the multiline text formfield that must be stored. (Should be a table field) See [Text fields overview](overview.md).  |

## Return values
< 0 error occurred; e.g. field is not a multiline text formfield on the form
-2 can not create a tmp file.
-3 the variabele text_field.text does not exist.
> 0 textfield-id saved in texttable.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
