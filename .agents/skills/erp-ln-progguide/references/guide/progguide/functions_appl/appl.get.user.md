# appl.get.user()

## Syntax:
`function long appl.get.user( const string name, ref string user(12), [ ref string session(13) ] )`

## Description
This retrieves the LN login name of the user who created the specified application lock.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the lock.  |
| `ref string` | `user(12)` |  The username of the user who created the lock.  |
| `[ ref string` | `session(13) ]` |  The session that has been locked.  |

## Return values
| | |
|---|---|
| 0 | success |
| -1 | lock not found |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Application locks: overview](application_locks_overview.md)

- [Application locks: synopsis](application_locks_synopsis.md)
