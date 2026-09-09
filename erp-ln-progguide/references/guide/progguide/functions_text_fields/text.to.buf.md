# text.to.buf()

## Syntax:
`function long text.to.buf( string text_field, string lang, long nr_lines, ref string buf(,), [ long rtf.text ] )`

## Description
This stores the text of a specified text field in a two-dimensional string array.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field that must be retrieved. See [Text fields overview](overview.md).  |
| `string` | `lang` |  This specifies the relevant language.  |
| `long` | `nr_lines` |  This specifies the maximum number of lines that can be stored in the buffer.  |
| `ref string` | `buf(,)` |  This specifies the buffer in which the text must be stored.  |
| `[ long` | `rtf.text ]` |  Set this argument to true if you want the text to be stored in RTF format instead of ASCII format. This is possible only when using a text group that supports RTF data.  |

## Return values
> 0 number of stored lines
0 error
- 1 no permission to store the text

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Note  When a database-text-field is entered as a long text-line without any LF or CR, the data is stored in tttxt010 over more the one entry, split in parts of 240 positions (tttxt010.seqe). In a script moving the database-text-field into the function text.to.buf() and the reference buffer is setup as text.buffer(240,40), all entries for the related database-text-field should appear in the buffer, as long as the tttxt010.seqe field has the value between 1 and 40. With the tttxt002.nlin value still at 1 for this text-entry, it appears that only the first 240 positions of this text are transferred into the text.buffer. Because of this, texts get lost in a script when applied.

## Related topics
- [Text fields overview](overview.md)

- [Text fields synopsis](synopsis.md)
