# text.rewrite()

## Syntax:
`function long text.rewrite( string text_field, string lang, string kw1, string kw2, string kw3, string kw4, string tgroup, string edit_opt, string tmp_file, [ long bidi, string rtf_file ] )`

## Description
This writes text from a specified file to a specified text field. The new text and new text attributes replace the existing text and text attributes.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field to which the file must be copied. See [Text fields overview](overview.md). If the specified text does not exist, nothing happens and the function returns 0.  |
| `string` | `lang` |  The language for which the text is to be rewritten.  |
| `string` | `kw1` |  Use these arguments to specify key words for the text.  |
| `string` | `kw2` |  |
| `string` | `kw3` |  |
| `string` | `kw4` |  |
| `string` | `tgroup` |  This specifies the name of the text group to which the text must be assigned. If you specify an empty string here, the text is assigned to the user's default group.  |
| `string` | `edit_opt` |  This specifies the type of window in which the text must be displayed.  |
| `string` | `tmp_file` |  The name of the file where the new text is stored. The contents of this file is changed before the text is stored, Long lines are wrapped to meet the line width of the text group to which the text is assigned.  |
| `[ long` | `bidi ]` |  Use this optional argument to indicate the text alignment. Possible values are: true text is right justified false text is left justified; this is the default option  |
| `[ string` | `rtf_file ]` |  The name of the file in which the RTF version of the text must be stored. This is an optional argument. The usage of this argument depends on the settings of the text group as defined in the tgroup argument. If this is an empty string, no text is retrieved and the function returns 0.  |

## Return values
> 0: success; returns the number of lines written to the text field
0: no such text
< 0: some error occurred
-1: no permission for text group

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
