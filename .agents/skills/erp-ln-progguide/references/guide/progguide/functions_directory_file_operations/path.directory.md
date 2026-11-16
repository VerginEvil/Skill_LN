# path.directory()

## Syntax:
`function string path.directory( const string path, [ long os.type ] )`

## Description
Returns the directory information for the specified path string.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path of a file or a directory  |
| `[ long` | `os.type ]` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
Directory information for path, or an empty string if path denotes a root directory or is empty, or if path does not contain directory information.
In most cases, the string returned by this function consists of all characters in the path up to but not including the last [path.dir.separator()](path.dir.separator.md). If the path consists of a root directory, such as "c:\", an empty string is returned. Note that this method does not support paths using "file:". Because the returned path does not include the [path.dir.separator()](path.dir.separator.md), passing the returned path back into the `path.directory()` method will result in the truncation of one folder level per subsequent call on the result string. For example, passing the path "C:\Directory\SubDirectory\test.txt" into the `path.directory()` method will return "C:\Directory\SubDirectory". Passing that string, "C:\Directory\SubDirectory", into `path.directory()` will result in "C:\Directory".

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string path(1024)

| Suppose Infor Enterprise Server is running on Unix
path = path.directory("/home/user/out")
| path = "/home/user"

path = path.directory("/home/user/tmp/")
| path = "/home/user/tmp"

path = path.directory("/")
| path = ""

path = path.directory("")
| path = ""

path = path.directory("test.doc")
| path = ""

| Dealing with Windows  paths
path = path.directory("c:\temp\test.doc", OS_WINDOWS_NT)
| path = "c:\temp"

path = path.directory("c:\temp\", OS_WINDOWS_NT)
| path = "c:\temp"

path = path.directory("c:\temp", OS_WINDOWS_NT)
| path = ""

path = path.directory("c:\", OS_WINDOWS_NT)
| path = ""

path = path.directory("", OS_WINDOWS_NT)
| path = ""
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
