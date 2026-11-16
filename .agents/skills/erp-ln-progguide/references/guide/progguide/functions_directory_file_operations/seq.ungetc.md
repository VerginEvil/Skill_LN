# seq.ungetc$()

## Syntax:
`function string seq.ungetc$( string char, long fp )`

## Description
This puts back a specified character, retrieved by [seq.getc$()](seq.getc.md). The character will be returned by the next *seq.getc$()* call on that file. This function works only if something has been read from the file and if the file is buffered. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.

## Arguments
| | | |
|---|---|---|
| `string` | `char` |  This puts back a specified character  |
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.  |

## Return values
The character written to the file. Or an empty string if end-of-file is reached or an error occurred.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
