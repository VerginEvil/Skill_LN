# get.bw.username()

## Syntax:
`function long get.bw.username( ref string username )`

## Description
This returns the Windows username of the user that started the BW client

## Arguments
| | | |
|---|---|---|
| `ref string` | `username` |    |

## Return values
1 (TRUE) Function succeeded, username is filled
0 (FALSE) Function failed, username is unchanged

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
