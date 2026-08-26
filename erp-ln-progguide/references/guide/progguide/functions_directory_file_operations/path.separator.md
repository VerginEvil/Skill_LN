# path.separator()

## Syntax:
`function string path.separator( [ long os.type ] )`

## Description
Returns a platform-specific separator character (":" or ";") used to separate path strings in environment variables.
Do not confuse this function with ` [path.dir.separator()](path.dir.separator.md)`.
If Infor Enterprise Server is running on UNIX, the returned separator is the colon (:); if Infor Enterprise Server is running on Windows, the returned separator is the semi-colon (;). By supplying the OS type this function will return the separator for the given OS type.

## Arguments
| | | |
|---|---|---|
| `[ long` | `os.type ]` |  when specified, the separator returned is the one for the given OS type; specify one of the following values: `OS_WINDOWS_NT`, `OS_UNIX`  |

## Return values
On Windows-based platforms, the value returned is the semicolon (;). On Unix platforms the value returned is the colon (:).

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1700.

## Example
```

string separator(1)

| Suppose Infor Enterprise Server is running on Unix
separator = path.separator()
| separator = ":"

| Get the Windows path separator
separator = path.separator(OS_WINDOWS_NT)
| separator = ";"
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
