# seq.getc$()

## Syntax:
`function string seq.getc$( long fp )`

## Description
This returns the next character from a specified file. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the file was opened. An empty string (a string of length 0) indicates either that the end-of-file has been reached or that an error has occurred.

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  fp is the file pointer returned by seq.open() when the file was opened..  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
