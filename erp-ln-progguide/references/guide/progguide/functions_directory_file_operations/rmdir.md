# rmdir()

## Syntax:
`function long rmdir( const string spath, [ boolean recursive ] )`

## Description
This deletes the specified directory (local or remote). The *path* argument must include the full path to the directory, including the host name, where appropriate. For example: "host!c:\usr".

## Arguments
| | | |
|---|---|---|
| `const string` | `spath` |  Path.  |
| `[ boolean` | `recursive ]` |  specify true if any subdirectories and files in the directory have | to be deleted as well  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2460 and
- Only allowed to remove within $BSE/appdata  Parameter recursive is not allowed if called within "tx" programs.
Note  This function is extended with parameter recursive from [TIV](../tiv/tiv_overview.md) [level 1900](../tiv/tiv_1900.md).

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
