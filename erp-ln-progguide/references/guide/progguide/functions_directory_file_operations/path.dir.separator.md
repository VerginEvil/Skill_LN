# path.dir.separator()

## Syntax:
`function string path.dir.separator( [ long os.type ] )`

## Description
Provides a platform-specific character used to separate directory levels in a path string that reflects a hierarchical file system organization.
If Infor Enterprise Server is running on UNIX, the returned directory separator is the forward slash ("/"); if Infor Enterprise Server is running on Windows, the returned directory separator is the backslash ("\"). By supplying the OS type this function will return the directory separator for the given OS type.

## Arguments
| | | |
|---|---|---|
| `[ long` | `os.type ]` |  when specified, the directory separator returned is the one for the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
The value is a slash ("/") for UNIX, and a backslash ("\") for the Windows operating systems.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string dir.separator(1)

| Suppose Infor Enterprise Server is running on Unix
dir.separator = path.dir.separator()
| dir.separator = "/"

| Get the Windows directory separator
dir.separator = path.dir.separator(OS_WINDOWS_NT)
| dir.separator = "\"
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
