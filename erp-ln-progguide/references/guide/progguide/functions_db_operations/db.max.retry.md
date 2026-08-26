# db.max.retry()

## Syntax:
`function long db.max.retry( )`

## Description
This function returns the value of the MAX_RETRY resource setting, which indicates how often the system may return to a retry point as a result of an abort in an update action.
This is a better alternative for getenv$("MAX_RETRY").

## Return values
The value of the MAX_RETRY resource.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Retry points](../functions_database_handling/retry_points.md)
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
