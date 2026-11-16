# path.has.extension()

## Syntax:
`function boolean path.has.extension( const string path, [ long os.type ] )`

## Description
Determines whether a path string includes a file name extension.
If Infor Enterprise Server is running on UNIX, the given path is interpreted as a Unix path; if Infor Enterprise Server is running on Windows, the path is interpreted as a Windows path. Optionally, this can be overridden, by supplying the OS type. When dealing with paths for the client (e.g. when using [seq.open.local()](../functions_client_file_access/seq.open.local.md), it is advised to always specify `OS_WINDOWS_NT`.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  the path string to search for an extension  |
| `[ long` | `os.type ]` |  when specified, the path is interpreted according to the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
true if the characters that follow the last directory separator (\ or /) in the path include a period (.) followed by one or more characters; otherwise, false.
Starting from the end of path, this method searches for a period (.) followed by at least one character. If this pattern is found before a [path.dir.separator()](path.dir.separator.md) character is encountered, this method returns true.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string path(1024)
boolean	ret

| Suppose Infor Enterprise Server is running on Unix
ret = path.has.extension("/home/user/test.doc")
| ret = true

ret = path.has.extension("/home/user/test")
| ret = false

ret = path.has.extension("/tmp.dir/test")
| ret = false

| Dealing with Windows paths
ret = path.has.extension("c:\temp\test.doc", OS_WINDOWS_NT)
| ret = true

ret = path.has.extension("c:\temp\test", OS_WINDOWS_NT)
| ret = false

ret = path.has.extension("c:\temp.dir\test", OS_WINDOWS_NT)
| ret = false
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
