# path.exists()

## Syntax:
`function boolean path.exists( const string path, [ long access_level ] )`

## Description
This function returns true if the given path exists, and false otherwise. If the current BSE is a tenant BSE and no absolute path is given, the path is interpreted as a relative path.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  The file or directory to check.  |
| `[ long` | `access_level ]` |  Optional, determines how to interpret the path if the current BSE is a tenant BSE:  |

## Return values
True if the file or directory exists, false otherwise

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2030.

## Example
```

boolean ret

ret = path.exists("somefile.txt", PATH_USER_LEVEL)
| If the current BSE is a tenant BSE this tests whether ${BSE}/appdata/somefile.txt exists
| Otherwise this tests whether somefile.txt exists in the current directory.

ret = path.exists("${BSE}/tmp/somefile.txt", PATH_SYSTEM_LEVEL)
| This tests whether ${BSE}/tmp/somefile.txt exists in both situations.
```

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
