# path.exists()

## Syntax:
`function boolean path.exists( const string path, [ long access_level ] )`

## Description
This function returns true if the given path exists, and false otherwise. If the current BSE is a tenant BSE and no absolute path is given, the path is interpreted as a relative path.

## Arguments
| | |
|---|---|
| PATH_USER_LEVEL | Default; the path is interpreted relative to $BSE/appdata |
| PATH_SYSTEM_LEVEL | The path is interpreted relative to $BSE |
This parameter has no effect if the current BSE is not a tenant BSE, the path will be used as-is in that case.
This parameter is deprecated as of [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md).

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
