# curl.sso.user.encode$()

## Syntax:
`function string curl.sso.user.encode$( const string User )`

## Description
...

## Arguments
| | | |
|---|---|---|
| `const string` | `User` |  Name of the SSO user  |

## Return values
Contains an escaped SSO user string

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [cURL handling overview](overview.md)
- [curl.escape.encode$()](curl.escape.encode$.md)
