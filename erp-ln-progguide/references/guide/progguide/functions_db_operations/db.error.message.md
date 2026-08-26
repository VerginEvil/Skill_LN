# db.error.message()

## Syntax:
`function string db.error.message( )`

## Description
Some errors returned by a database action have an associated error message. This message provides additional information about the error. Use the *db.error.message()* function to retrieve the error message (if any) associated with the most recent error code returned by a database action.

## Return values
The error message associated with the most recent error that occurred. Or an empty string if no message is associated with the error.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
