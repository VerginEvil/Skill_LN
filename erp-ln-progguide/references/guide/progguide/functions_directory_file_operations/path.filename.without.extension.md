# path.filename.without.extension()

## Syntax:
`function string path.filename.without.extension( const string path, [ long os.type ] )`

## Description
Returns the filename of the specified path string without the extension.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path string of the file  |
| `[ long` | `os.type ]` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
The string returned by [path.filename()](path.filename.md), minus the last period (.) and all characters following it.
This method does not verify that the path or file name exists.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string path(1024)

| Suppose Infor Enterprise Server is running on Unix
path = path.filename.without.extension("/home/user/test.txt")
| path = "test"

path = path.filename.without.extension("test.txt")
| path = "test"

path = path.filename.without.extension("")
| path = ""

| Dealing with Windows paths
path = path.filename.without.extension("c:\temp\test.txt", OS_WINDOWS_NT)
| path = "test"

path = path.filename.without.extension("c:\test.txt", OS_WINDOWS_NT)
| path = "test"

path = path.filename.without.extension("test.txt", OS_WINDOWS_NT)
| path = "test"

path = path.filename.without.extension("", OS_WINDOWS_NT)
| path = ""
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
