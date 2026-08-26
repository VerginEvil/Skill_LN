# switch.to.role()

## Syntax:
`function long switch.to.role( string role )`

## Description
This switches the active user personalization role of the user to another role. The role must be known for the user, otherwise the role is not changed.

## Arguments
| | | |
|---|---|---|
| `string` | `role` |  The new active user personalization role.  |

## Return values
0: active role switched
-1: role is unknown for the user
-2: error in reading User Roles

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function should only be used before starting a new session, so that session starts with the new role. It cannot be used to change the role of a running session.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
