# path.extension()

## Syntax:
`function string path.extension( const string path, [ long os.type ] )`

## Description
Returns the extension of the specified path string.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path string from which to get the extension  |
| `[ long` | `os.type ]` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
The extension of the specified path (including the period "."), or an empty string. If path is an empty string, or if path does not have extension information, this function returns an empty string.
The extension of path is obtained by searching path for a period (.), starting with the last character in path and continuing toward the start of path. If a period is found before a [path.dir.separator()](path.dir.separator.md) character, the returned string contains the period and the characters after it; otherwise, an empty string is returned.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string ext(10)

| Suppose Infor Enterprise Server is running on Unix
ext = path.extension("/home/user/test.txt")
| ext = ".txt"

ext = path.extension("/home/user/test.")
| ext = ""

ext = path.extension("/home/user/test.dir/test")
| ext = ""

ext = path.extension("/home/user/testdir/test")
| ext  = ""

| Dealing with Windows paths
ext  = path.extension("c:\temp\testdir\test.txt", OS_WINDOWS_NT)
| ext = ".txt"

ext = path.extension("c:\temp\testdir\test.", OS_WINDOWS_NT)
| ext = ""

ext = path.extension("c:\temp\testdir\test.dir\test", OS_WINDOWS_NT)
| ext = ""

ext = path.extension("c:\temp\testdir\test", OS_WINDOWS_NT)
| ext = ""
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
