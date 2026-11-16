# file.chmod()

## Syntax:
`function long file.chmod( const string file, long mode )`

## Description
This sets the access permissions for a specified file.

## Arguments
| | |
|---|---|
| S_IRWXU | read, write, execute |
| S_IRUSR | read |
| S_IWUSR | write |
| S_IXUSR | execute, search |
| S_ISUID | user id on execution |
Group
| | |
|---|---|
| S_IRWXG | read, write, execute |
| S_IRGRP | read |
| S_IWGRP | write |
| S_IXGRP | execute, search |
| S_ISGID | group id on execution |
Other (UNIX only)
| | |
|---|---|
| S_IRWXO | read, write, execute |
| S_IROTH | read |
| S_IWOTH | write |
| S_IXOTH | execute, search |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable. |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Setting file access permissions is a system-dependent feature. To enable applications to be system independent, this function does not return an error code when a particular feature is unavailable.

## Related topics
- [Directory and file operations overview](overview.md)

- [Directory and file operations synopsis](synopsis.md)
