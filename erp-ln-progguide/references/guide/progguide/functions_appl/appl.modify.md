# appl.modify()

## Syntax:
`function long appl.modify( const string name, long old.owner, long new.owner )`

## Description
This changes the owner of a specified application lock. That is, it links the application lock to another 4GL process in the same bshell.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the application lock.  |
| `long` | `old.owner` |  The process ID of the current owner.  |
| `long` | `new.owner` |  The process ID of the new owner.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | lock not found |
| -3 | internal error |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1075.

## Related topics
- [Application locks: overview](application_locks_overview.md)
- [Application locks: synopsis](application_locks_synopsis.md)
