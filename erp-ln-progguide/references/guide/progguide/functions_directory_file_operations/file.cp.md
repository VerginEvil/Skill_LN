# file.cp()

## Syntax:
`function long file.cp( const string source, const string target )`

## Description
This copies a specified source file to a specified target file. Both files can be either local or remote. They can also be on different hosts (provided that the bshell can access both hosts).

## Arguments
| | | |
|---|---|---|
| `const string` | `source` |  Source file.  |
| `const string` | `target` |  Target file.  |

## Return values
| | |
|---|---|
| >= 0 | Success. (If *source* and *target* are the same local file, then *e* is set to 1, otherwise to 0.)  |
| < 0 | Error. The [error code](../errors/overview.md) is stored in the *e* variable.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Directory and file operations overview](overview.md)
- [Directory and file operations synopsis](synopsis.md)
