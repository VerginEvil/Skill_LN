# seq.open.bse.file()

## Syntax:
`function long seq.open.bse.file( string file, string openmode, [ ref string pathnm ] )`

## Description
The function should be used when there is a requirement to open a file in a BSE. It is specifically useful in a multi-tenant environment where the construction like `seq.open("${BSE}/file:${BSE_REM}!${BSE}/file")` is not correct because ${BSE} then refers to the tenant's subdirectory within the landlord BSE.

## Arguments
| | |
|---|---|
| "r" | Open for reading. The current file position is placed at the *start* of the file. |
| "w" | Open for writing. The file is created if it does not already exist. The current file position is placed at the *start* of the file. |
| "a" | Open for writing. The file is created if it does not already exist. The current file position is placed at the *end* of the file. The file position is placed at end of the file before every write statement, even if the previous file action was a [seq.seek()](seq.seek.md). |
| "x" | Open for writing. This is the same as "w", except that the function fails if the file already exists. |
| "r+" | Same as "r", but the file can also be written to. |
| "w+" | Same as "w", but the file can also be read. |
| "a+" | Same as "a", but the file can also be read. |
| "x+" | Same as "x", but the file can also be read. |
| Use the following modes to indicate whether the file is a binary or a text file. You can combine one of these modes with any one of the previous modes (for example, "rt+"). |  |
| "b" | Use for binary files. This is the default mode and need not be specified. |
| "t" | The line separator(s) for text-files are different on Windows NT and UNIX systems. CRLF on the former; LF only on the latter. In addition, a Windows NT text file can include an EOF-character (^Z) that indicates the end of the file. This character should not be returned to a program reading the file. So, you *must* specify the "t" option when reading from or writing to a text file on Windows NT systems (for example, "at+".) This ensures that line separators and EOF characters are handled correctly. Never use the "t" option when opening a binary file; on Windows NT systems this will corrupt the file data. The "t" option has no effect on UNIX systems. |

## Return values
| | |
|---|---|
| >= 1 | Success; File pointer returned for use in subsequent operations. |
| < 1 | Error; that is, the negative value of the system error (for example, for a permission error, the system returns 13 and the function returns -13, or if the internal table is full, the function returns -EAGAIN). |

## Context
This function is implemented in the porting set and can be used in all script types.
Safety  Although this function might seem unsafe, it is a trusted function that may be used in client code.
Notes  When you open a file for reading and writing, you cannot follow an output operation directly by an input operation. You must call [seq.seek()](seq.seek.md) or [seq.rewind()](seq.rewind.md) to reset the current file position before the input operation.
Also, you cannot follow an input operation directly by an output operation, unless the input operation encounters the end-of-file indicator. You must call [seq.seek()](seq.seek.md) or [seq.rewind()](seq.rewind.md) to reset the current file position before the output operation.
The character `";"` is not supported in a file name. The `";"` is used as a path separator. `Seq.open.bse.file("a;b","r")` means open file `"a"`, and if this fails open file `"b"`.

## Example
```

long ret
long fd
string relative.path(512)
string path(512)

| open "lib/zoneinfo/America/New_York" present inside $BSE.
path = "-"
relative.path = "lib/zoneinfo/America/New_York"
fd = seq.open.bse.file( relative.path, "r", path )

ret = seq.close(fd)
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
