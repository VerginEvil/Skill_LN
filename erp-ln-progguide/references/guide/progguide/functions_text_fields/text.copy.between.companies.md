# text.copy.between.companies()

## Syntax:
`function long text.copy.between.companies( string text_field_to, string text_field_from, long source_company, long target_company, string kw1, string kw2, string kw3, string kw4, string tgroup, string edit_opt, [ boolean txt.defaults ] )`

## Description
This copies the entire text of a specified text field, for all languages, from one company to another.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field_to` |  The name of the new text field. See [Text fields overview](overview.md). This returns the text number for the new text field.  |
| `string` | `text_field_from` |  The name of the text field that must be copied. See [Text fields overview](overview.md).  |
| `long` | `source_company` |  This specifies the source company.  |
| `long` | `target_company` |  This specifies the destination company.  |
| `string` | `kw1` |  Use these arguments to specify key words for the new text. If you specify one or more of these arguments as an empty string, the corresponding key word(s) are copied from the original text. It is possible, for example, to specify two new key words and to copy the other two from the original text.  |
| `string` | `kw2` |    |
| `string` | `kw3` |    |
| `string` | `kw4` |    |
| `string` | `tgroup` |  This specifies the name of the text group to which the new text must be assigned. If you specify an empty string here, the text is assigned to the user's default group.  |
| `string` | `edit_opt` |  This specifies the type of window in which the text must be displayed.  |
| `[ boolean` | `txt.defaults ]` |  This indicates if text defaults must be copied. If omitted, text defaults are not copied.  |

## Return values
> 0 success; returns the number of lines copied
-1 Error in defaults or permissions
-2 No text copied.
-3 Error in creating defaults (textgroup or textwindows)
In case of textauthorizations are set to "Use" value of textnumber in variable tm.field.from has been assigned to tm.field.to.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
