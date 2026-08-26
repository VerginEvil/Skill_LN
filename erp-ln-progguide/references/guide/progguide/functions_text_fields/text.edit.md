# text.edit()

## Syntax:
`function long text.edit( string text_field, string lang, string kw1, string kw2, string kw3, string kw4, string tgroup, string edit_opt, long mode )`

## Description
This opens an edit window in which the specified text can be edited. If the text number associated with the specified text (i.e., the value of the field with name *text_field*) is 0, the text manager prompts the user to confirm whether or not a new text must be created. After editing, the text number is stored in the field with name *text_field*.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field. See [Text fields overview](overview.md). The text number is read from this field, and if that number is 0, the new text number is stored in this field.  |
| `string` | `lang` |  The language for which the text is to be edited.  |
| `string` | `kw1` |  Use these arguments to specify the key words for the text.  |
| `string` | `kw2` |  |
| `string` | `kw3` |  |
| `string` | `kw4` |  |
| `string` | `tgroup` |  This specifies the name of the text group to which the new text must be assigned. If you specify an empty string here, the text is assigned to the user's default group.  |
| `string` | `edit_opt` |  This specifies the type of window in which the text must be displayed.  |
| `long` | `mode` |  This species the text mode. Possible values are: 1 read-only 3 read and write  |

## Return values
The text number (0 if there was no text, and the user did not create a new one). Or < 0 if an error occurred (-1 means 'no permission').

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
