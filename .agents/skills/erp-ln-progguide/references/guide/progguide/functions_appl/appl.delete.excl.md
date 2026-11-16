# appl.delete.excl()

## Syntax:
`function long appl.delete.excl( const string name )`

## Description
This removes a specified exclusive application lock. Only the owner of the lock can delete it. And a lock can be deleted only from within the same process in which it was set.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The lock name  |

## Return values
| | |
|---|---|
| 0 | Lock removed |
| -1 | Lock not found |
| -3 | Internal error |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Application locks: overview](application_locks_overview.md)

- [Application locks: synopsis](application_locks_synopsis.md)
