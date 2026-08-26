# seq.gets()

## Syntax:
`function long seq.gets( ref string line, long nrbytes, long fp, [ long mode, ref long there.was.more ] )`

## Description
This reads one or more characters from a specified file.

## Arguments
| | | |
|---|---|---|
| `ref string` | `line` |  This stores the retrieved characters.  |
| `long` | `nrbytes` |  The maximum number of bytes to be read. Note that the function stops retrieving characters when a new line character is read or when the end of file is reached.  |
| `long` | `fp` |  The pointer to the file from which the characters are to be read, as returned by [seq.open()](seq.open.md) when the file was opened.  |
| `[ long` | `mode ]` |  Use this optional argument to specify the read mode for seq.gets(). Possible values are:  |
| `[ ref long` | `there.was.more ]` |  When characters are discarded in GETS_NORMAL or GETS_SKIP_ALL mode, or when more characters are available in the line (but the buffer is full) in GETS_ALL_CHARS mode, this argument is set to 1. Otherwise, the argument returns 0.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; probably *fp* not connected or end of file reached.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
