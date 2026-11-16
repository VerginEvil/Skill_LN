# user.exists()

## Syntax:
`function boolean user.exists( const string username )`

## Description
This checks whether a specified user is defined on the system. Whether user names are case-sensitive or case-insensitive is a system-dependent feature.

## Arguments
| | | |
|---|---|---|
| `const string` | `username` |    |

## Return values
TRUE user exists
FALSE user does not exist

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
