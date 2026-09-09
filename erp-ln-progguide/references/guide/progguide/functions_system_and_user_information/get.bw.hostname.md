# get.bw.hostname()

## Syntax:
`function long get.bw.hostname( ref string hostname )`

## Description
This returns the hostname of the bw client (if available)

## Arguments
| | | |
|---|---|---|
| `ref string` | `hostname` |    |

## Return values
1 (TRUE) Function succeeded, hostname is filled
0 (FALSE) Function failed, hostname is unchanged

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
