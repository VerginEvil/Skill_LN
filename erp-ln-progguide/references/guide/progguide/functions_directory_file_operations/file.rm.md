# file.rm()

## Syntax:
`function long file.rm( const string path )`

## Description
This deletes a specified local or remote file. The *path* argument must include the full path to the file, including the host name, where appropriate.

## Arguments
| | | |
|---|---|---|
| `const string` | `path` |  Remote or local file.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
