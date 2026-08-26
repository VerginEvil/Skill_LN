# file.mv()

## Syntax:
`function long file.mv( const string source, const string target )`

## Description
This moves a specified source file to the location specified in the *target* argument. The file can be either local or remote. Both source and target must be on the same host.

## Arguments
| | | |
|---|---|---|
| `const string` | `source` |  Source file.  |
| `const string` | `target` |  Target file.  |

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
