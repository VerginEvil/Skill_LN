# text.read()

## Syntax:
`function long text.read( string text_field, string lang, string kw1, string kw2, string kw3, string kw4, ref string tgroup, ref string edit_opt, string tmp_file, long lock, [ string rtf_file ] )`

## Description
This reads a specified text and stores it in a temporary file. If this file already exists, it will be overwritten.

## Arguments
| | | |
|---|---|---|
| `string` | `text_field` |  The name of the text field that must be read. See [Text fields overview](overview.md). If the text number of the specified field is 0, a subprocess is started, which lists the texts associated with the current company and enables the user to select the text to be read. If no text is found, or if you abort the subprocess, *text_field* returns 0. Otherwise, it returns the text number of the retrieved text.  |
| `string` | `lang` |  The language for which the text must be retrieved.  |
| `string` | `kw1` |  These return the key words associated with the specified text.  |
| `string` | `kw2` |  |
| `string` | `kw3` |  |
| `string` | `kw4` |  |
| `ref string` | `tgroup` |  This returns the name of the text group to which the text is assigned.  |
| `ref string` | `edit_opt` |  This returns the default window type for the text.  |
| `string` | `tmp_file` |  The name of the file in which the text must be stored. If this is an empty string, no text is retrieved and the function returns 0.  |
| `long` | `lock` |  By default, a lock is applied to the text field when it is read. To read the field without lock, set this argument to 0.  |
| `[ string` | `rtf_file ]` |  The name of the file in which the RTF version of the text must be stored. This is an optional argument. The usage of this argument depends on the settings of the text group as defined in the tgroup argument. If this is an empty string, no text is retrieved and the function returns 0.  |

## Return values
> 0 success; returns the number of lines read
0 no text found or subprocess aborted
-1 no permission

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [Text fields overview](overview.md)
- [Text fields synopsis](synopsis.md)
