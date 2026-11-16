# text.set.keywords()

## Syntax:
`function boolean text.set.keywords( string text_field, string keyword1, string keyword2, string keyword3, string keyword4 )`

## Description
This stores keyword(s) to the specified multiline text formfield. When the field can be edited with the textmanager (also), attr.textkw1$, attr.textkw2$, attr.textkw3$, attr.textkw4$ in the on.choice of 4gl-section choice.text.manager. In session "Texts overview" (tttxt1500m000) you can search for texts based on keywords.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the multiline text formfield that must be retrieved. See [Text fields overview](overview.md).  |
| `string` | `keyword1` |  First keyword of textfield. When not specifying any keyfield, this first keyfield is filled with fieldname.  |
| `string` | `keyword2` |  Optional. Second keyword of textfield.  |
| `string` | `keyword3` |  Optional. Third keyword of textfield.  |
| `string` | `keyword4` |  Optional. Fourth keyword of textfield.  |

## Return values
false field is not a multiline text formfield on the form
true function successful

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
Note  This function can be used in the when.field.changes section of the multiline text formfield.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
