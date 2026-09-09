# path.combine()

## Syntax:
`function string path.combine( const string path,..., long os.type )`

## Description
Combines one ore more strings into a path.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  a path part  |
|  | `...` | optional path parts |
| `long` | `os.type` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`. Note: this must be the last argument.  |

## Return values
The combined paths.

- If one of the subsequent paths is an absolute path, then the combine operation resets starting with that absolute path, discarding all previous combined paths.

- Zero-length strings are omitted from the combined path.

- The parameters are not parsed if they have white space.

- Not all invalid characters for directory and file names are interpreted as unacceptable by the `path.combine` function, because you can use these characters for search wildcard characters. For example, while `path.combine("c:\", "*.txt")` might be invalid if you were to create a file from it, it is valid as a search string. It is therefore successfully interpreted by the `path.combine` function.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string path(1024)

| Suppose Infor Enterprise Server is running on Unix, but we want to deal with Windows paths
path = path.combine("c:\temp", "test", "bla", "mydoc.doc", OS_WINDOWS_NT)
| path = "c:\temp\test\bla\mydoc.doc"

path = path.combine("c:\temp", "test", "c:\bla", "mydoc.doc", OS_WINDOWS_NT)
| path = "c:\bla\mydoc.doc"

path = path.combine("c:\temp", "", "bla", "mydoc.doc", OS_WINDOWS_NT)
| path = "c:\temp\bla\mydoc.doc"

path = path.combine("c:\temp\", "x\", "bla", "mydoc.doc", OS_WINDOWS_NT)
| path = "c:\temp\x\bla\mydoc.doc"

path = path.combine("", "")
| path = ""
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
