# seq.open()

## Syntax:
`function long seq.open( string file, string openmode, [ ref string pathnm ] )`

## Description
This opens a specified file. It uses the file $BSE/lib/fd *ver.pack_combination* to find the file. *ver* refers to a particular release of the software; *pack_combination* refers to a particular package combination (see [pathname()](pathname.md)).

## Arguments
| | | |
|---|---|---|
| `string` | `file` |  The file name.  |
| `string` | `openmode` |  The mode in which the file must be opened. This can be one of the following options:  |
| `[ ref string` | `pathnm ]` |  This returns the full path to the file.  |

## Return values
| | |
|---|---|
| >= 1 | Success; File pointer returned for use in subsequent operations.  |
| < 1 | Error; that is, the negative value of the system error (for example, for a permission error, the system returns 13 and the function returns -13, or if the internal table is full, the function returns -EAGAIN).  |

## Context
This function is implemented in the porting set and can be used in all script types.
Safety  Although this function might seem unsafe, it is a trusted function that may be used in client code.
Notes  When you open a file for reading and writing, you cannot follow an output operation directly by an input operation. You must call [seq.seek()](seq.seek.md) or [seq.rewind()](seq.rewind.md) to reset the current file position before the input operation.
Also, you cannot follow an input operation directly by an output operation, unless the input operation encounters the end-of-file indicator. You must call [seq.seek()](seq.seek.md) or [seq.rewind()](seq.rewind.md) to reset the current file position before the output operation.
The character `";"` is not supported in a file name. The `";"` is used as a path separator. `Seq.open("a;b","r")` means open file `"a"`, and if this fails open file `"b"`. (Note: this behavior is used in the Tools: `seq.open("${BSE}/lib/dtopt2;${BSE_REM}!${BSE}/lib/dtopt2","r"))`.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
