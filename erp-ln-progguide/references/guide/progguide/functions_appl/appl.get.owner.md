# appl.get.owner()

## Syntax:
`function long appl.get.owner( const string name, ref long owner, [ ref string session(13) ] )`

## Description
This retrieves the owner of the application lock.

## Arguments
| | | |
|---|---|---|
| `const string` | `name` |  The name of the lock.  |
| `ref long` | `owner` |  The process ID of the current owner of the application lock.  |
| `[ ref string` | `session(13) ]` |  The session that has been locked.  |

## Return values
0 is successful and -1 lock not found or any other error

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2360.

## Related topics
- [Application locks: overview](application_locks_overview.md)
- [Application locks: synopsis](application_locks_synopsis.md)
