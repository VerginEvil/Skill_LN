# path.change.extension()

## Syntax:
`function string path.change.extension( const string path, const string extension, [ long os.type ] )`

## Description
Changes the extension of the specified path string. By default the path string is interpreted according to the Operating System of the Infor Enterprise Server server.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path string to modify  |
| `const string` | `extension` |  the new extension (with or without a leading period). Specify an empty string to remove the existing extension from the path  |
| `[ long` | `os.type ]` |  when specified, the path string is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
The modified path information.
If path is an empty string (""), the extension (with a leading period) is returned. If extension is an empty string, the returned string contains the specified path with its extension removed. If path has no extension, and extension is not empty, the returned path string contains extension appended to the end of path.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

string	path(1024)

| Suppose Infor Enterprise Server is running on Unix
path = path.change.extension("/home/user/my_file.txt", "doc")
| path = "/home/user/my_file.doc"

path = path.change.extension("/home/user/my_file.txt", ".doc")
| path = "/home/user/my_file.doc"

path = path.change.extension("/home/user/my_file", "doc")
| path = "/home/user/my_file.doc"

path = path.change.extension("/home/user/my_file.", "doc")
| path = "/home/user/my_file.doc"

path = path.change.extension("/home/user/my_file.", ".doc")
| path = "/home/user/my_file.doc"

path = path.change.extension("/home/user/my.file/", "doc")
| path = "/home/user/my.file/.doc"

path = path.change.extension("/home/user/my_file.txt", "")
| path = "/home/user/my_file"

path = path.change.extension("/home/user/my_file", "")
| path = "/home/user/my_file."

path = path.change.extension("", ".xls")
| path = ".xls"

| client file path
path = path.change.extension("c:\data\my_file.doc", ".xls", OS_WINDOWS_NT)
| path = "c:\data\my_file.xls"
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
