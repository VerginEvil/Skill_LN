# text.write()

## Syntax:
`function long text.write( string text_field, string lang, string kw1, string kw2, string kw3, string kw4, string tgroup, string edit_opt, string tmp_file, [ long bidi, string rtf_file, long word.wrap ] )`

## Description
This adds a new text to the text manager and assigns a new text number to the text.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the new text field. See [Text fields overview](overview.md). This returns the text number for the new field.  |
| `string` | `lang` |  This specifies the language for the new text.  |
| `string` | `kw1` |  Use these arguments to specify key words for the text.  |
| `string` | `kw2` |    |
| `string` | `kw3` |    |
| `string` | `kw4` |    |
| `string` | `tgroup` |  This specifies the name of the text group to which the text must be assigned. If you specify an empty string here, the text is assigned to the user's default group.  |
| `string` | `edit_opt` |  This specifies the type of window in which the text must be displayed.  |
| `string` | `tmp_file` |  The name of the file where the text for the new field is stored. The contents of this file is changed before the text is stored, Long lines are wrapped to meet the line width of the text group to which the text is assigned.  |
| `[ long` | `bidi ]` |  Use this optional argument to indicate the text alignment. Possible values are: true text is right justified false text is left justified; this is the default option  |
| `[ string` | `rtf_file ]` |  The name of the file in which the RTF version of the text must be stored. This is an optional argument. The usage of this argument depends on the settings of the text group as defined in the tgroup argument. If this is an empty string, no text is retrieved and the function returns 0.  |
| `[ long` | `word.wrap ]` |  Use this optional argument when text must not be wrapped, this means no en-of-line characters will be added. 1: Text must be wrapped, this means end-of-line characters will be added. This is the default 0: Text must not be wrapped, this means no end-of-line characters will be added.  |

## Return values
> 0: success; returns the number of lines written
< 0: error

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
