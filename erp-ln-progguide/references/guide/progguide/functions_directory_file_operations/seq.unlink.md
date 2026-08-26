# seq.unlink()

## Syntax:
`function long seq.unlink( string path_name(512) )`

## Description
This deletes the file indicated by the *path_name* argument.

## Arguments
| | | |
|---|---|---|
| `string` | `path_name(512)` |  Path name argument.  |

## Return values
| | |
|---|---|
| >= 0 | Success. |
| < 0 | Error; The negative value of the operating system error.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
