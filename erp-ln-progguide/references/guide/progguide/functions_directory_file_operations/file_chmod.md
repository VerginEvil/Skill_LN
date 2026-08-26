# file.chmod()

## Syntax:
`function long file.chmod( const string file, long mode )`

## Description
This sets the access permissions for a specified file.

## Arguments
| | | |
|---|---|---|
| `const string` | `file` |  The name of the file.  |
| `long` | `mode` |  The type of access permissions that must be set. This can be a combination of the following values: User/owner  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable.  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  Setting file access permissions is a system-dependent feature. To enable applications to be system independent, this function does not return an error code when a particular feature is unavailable.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
