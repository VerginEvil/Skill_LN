# seq.gets()

## Syntax:
`function long seq.gets( ref string line, long nrbytes, long fp, [ long mode, ref long there.was.more ] )`

## Description
This reads one or more characters from a specified file.

## Arguments
| | |
|---|---|
| GETS_NORMAL | The function continues reading characters until either the buffer (line) is full, a new line character is read, or EOF is reached. If the buffer is full, any remaining characters on the line being read are discarded. This is the default mode. |
| GETS_ALL_CHARS | The function continues reading characters until either the buffer (line) is full, a new line character is read, or EOF is reached. If the buffer is full, the next seq.gets() call starts reading at the point where the current seq.gets() finished. The use of this mode ensures that all characters available in input file are eventually returned. |
| GETS_SKIP_ALL | This is the same as GETS_NORMAL, except that if the last line in the file does not end with a new line character, that line is discarded completely and EOF is returned. |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error; probably *fp* not connected or end of file reached. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
