# text.copy()

## Syntax:
`function long text.copy( string text_field_to, string text_field_from, string kw1, string kw2, string kw3, string kw4, string tgroup, string edit_opt )`

## Description
This makes a copy of the entire text of a specified text field, for all languages, and assigns it a new text number.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field_to` |  The name of the new text field. See [Text fields overview](overview.md). This returns the text number for the new text field.  |
| `string` | `text_field_from` |  The name of the text field that must be copied. See [Text fields overview](overview.md).  |
| `string` | `kw1` |  Use these arguments to specify key words for the new text. If you specify one or more of these arguments as an empty string, the corresponding key word(s) are copied from the original text. It is possible, for example, to specify two new key words and to copy the other two from the original text.  |
| `string` | `kw2` |    |
| `string` | `kw3` |    |
| `string` | `kw4` |    |
| `string` | `tgroup` |  This specifies the name of the text group to which the new text must be assigned. If you specify an empty string here, the text is assigned to the user's default group.  |
| `string` | `edit_opt` |  This specifies the type of window in which the text must be displayed.  |

## Return values
> 0 success; returns the number of lines copied
0 the text_field_from = 0, no source text number
-1 error; no permission for this text field
-2 No text copied.
In case of textauthorizations are set to "Use" value of textnumber in variable tm.field.from has been assigned to tm.field.to.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
This example copies the text from the text field tttxt008.help to a new text field named tttxt008.docu. A new text number is created for tttxt008.docu and this is returned in the first argument. Key words 1 and 2 are new. Key words 3 and 4 are copied from the original text.
```

ret=TEXT.COPY("tttxt008.docu", "tttxt008.help", "docu", "help", "",
                "", "", "")
```

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
