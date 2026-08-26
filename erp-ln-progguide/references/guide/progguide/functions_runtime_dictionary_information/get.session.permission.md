# get.session.permission()

## Syntax:
`function long get.session.permission( string session(13) )`

## Description
Retrieves the permission of the session ( *session*) in a bit pattern (see return values). Each of the listed 'return values' represents one bit. Multiple values can be bitwise OR-ed into one pattern and returned by the function. In cases of internal errors in the function, the value SESSION_NO_PERMISSION will be returned.

## Arguments
| | | |
|---|---|---|
| `string` | `session(13)` |  |

## Return values
SESSION_NO_PERMISSION
SESSION_DELETE_PERMISSION
SESSION_INSERT_PERMISSION
SESSION_MODIFY_PERMISSION
SESSION_DISPLAY_PERMISSION
SESSION_PRINT_PERMISSION

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Runtime dictionary information overview and synopsis](overview_and_synopsis.md)
