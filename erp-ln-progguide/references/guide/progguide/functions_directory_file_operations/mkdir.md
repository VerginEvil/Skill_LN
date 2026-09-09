# mkdir()

## Syntax:
`function long mkdir( string path_name$, [ long access_level ] )`

## Description
This creates the specified directory. You must have write permission in the parent directory to do this. Access permissions for the new directory are set to read, write, and execute for all users.

## Arguments
| | |
|---|---|
| PATH_USER_LEVEL | Default; the path is interpreted relative to $BSE/appdata |
| PATH_SYSTEM_LEVEL | The path is interpreted relative to $BSE |
This parameter has no effect if the current BSE is not a tenant BSE, the path will be used as-is in that case.
This parameter is deprecated as of [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [level 2200](../tiv/tiv_2200.md).

## Return values
| | |
|---|---|
| >= 0 | Success. (If the return value is 0 then you can be sure that the directory existed already.) |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable. |

## Context
This function is implemented in the porting set and can be used in all script types.
Note  This function is moved back from 4GL Engine to Portingset with [bshell TIV](../tiv/tiv_overview.md) [level 2140](../tiv/tiv_2140.md). This function is extended with parameter access_level from [TIV](../tiv/tiv_overview.md) [level 2030](../tiv/tiv_2030.md).

## Example
```

long ret

ret = mkdir("somedir", PATH_USER_LEVEL)
| If the current BSE is a tenant BSE this creates the directory ${BSE}/appdata/somedir
| Otherwise this creates the directory somedir in the current directory.

ret = mkdir("${BSE}/tmp/somedir", PATH_SYSTEM_LEVEL)
| This creates the directory ${BSE}/tmp/somedir in both situations.
```

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
