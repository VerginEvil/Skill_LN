# path.filename()

## Syntax:
`function string path.filename( const string path, [ long os.type ] )`

## Description
Returns the filename and extension of the specified path string.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path string from which to obtain the filename and the extension  |
| `[ long` | `os.type ]` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
The characters after the last directory character in path. If the last character of path is a directory or volume separator character, this method returns an empty string. If path is an empty string, this function returns an empty string as well.
The separator character used to determine the start of the file name is ` [path.dir.separator()](path.dir.separator.md)`.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string path(1024)

| Suppose Infor Enterprise Server is running on Unix
path = path.filename("/home/user/test.txt")
| path = "test.txt"

path = path.filename("test.txt")
| path = "test.txt"

path = path.filename("")
| path = ""

| Dealing with Windows paths
path = path.filename("c:\temp\test.txt", OS_WINDOWS_NT)
| path = "test.txt"

path = path.filename("c:\test.txt", OS_WINDOWS_NT)
| path = "test.txt"

path = path.filename("test.txt", OS_WINDOWS_NT)
| path = "test.txt"

path = path.filename("", OS_WINDOWS_NT)
| path = ""
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
