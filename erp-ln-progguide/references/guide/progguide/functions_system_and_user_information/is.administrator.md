# is.administrator()

## Syntax:
`function boolean is.administrator( )`

## Description
This checks whether or not the user that is running the bshell has administrator rights on the server that the bshell is running. On UNIX systems, the function returns TRUE if the user has root access to the system. On Windows NT systems, the function returns TRUE if the user belongs to the administrator group.

## Return values
TRUE user has administrator rights
FALSE user does not have administrator rights

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [System and user information overview and synopsis](overview_and_synopsis.md)
