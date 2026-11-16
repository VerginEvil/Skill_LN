# seq.tell()

## Syntax:
`function long seq.tell( long fp )`

## Description
This returns the current file position, relative to the beginning of the file. The file position is measured in bytes. *fp* is the file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.
Take care when using this function on files that have been opened in append mode (that is, with the *openmode* argument set to a or a+). Before calling *seq.tell()*, always call [seq.flush()](seq.flush.md) after you have written to the file with [seq.write()](seq.write.md).

## Arguments
| | | |
|---|---|---|
| `long` | `fp` |  The file pointer returned by [seq.open()](seq.open.md) when the particular file was opened.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error; probably *fp* not connected. |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
