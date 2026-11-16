# text.buf.to.field()

## Syntax:
`function boolean text.buf.to.field( string text_field, string buf )`

## Description
This function stores the text of a buffer in the specified multiline text formfield. This is only relevant for multiline text formfields in a non-maintable session. An additional 'display' of this field is needed to see the changes on the form.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the multiline text formfield that must be retrieved. See [Text fields overview](overview.md).  |
| `string` | `buf` |  This specifies the buffer to be set in the multiline text formfield.  |

## Return values
true text field changed.
false field is not a multiline text formfield.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
