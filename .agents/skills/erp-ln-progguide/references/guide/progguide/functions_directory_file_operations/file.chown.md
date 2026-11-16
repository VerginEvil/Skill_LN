# file.chown()

## Syntax:
`function long file.chown( string file, string user, string group )`

## Description
This changes the owner and/or group of a file. You can use a single call to change both the owner and the group. Alternatively, you can specify either the *user* argument or the *group* argument as an empty string.

## Arguments
| | | |
|---|---|---|
| `string` | `file` |  The name of the file.  |
| `string` | `user` |  The new owner of the file.  |
| `string` | `group` |  The new group of the file.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. See [error codes](../errors/overview.md). |
*Internal note:* For robust 3GL code, and to prevent mistakes when mixing different file-related functions, the return value should be interpreted as described above. The current implementation returns 0 on success and -1 on failure.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Setting users and groups for files is a system-dependent feature. To enable applications to be system independent, this function does not return an error code when a particular feature is unavailable.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
