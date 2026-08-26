# db.set.error.bypass.off()

## Syntax:
`function void db.set.error.bypass.off( )`

## Description
This function resets the values of error.bypass and error.bypass.with.retry to the previous values. The function must be called exactly once for each time the function db.set.error.bypass.on() is called. Calling this function more often than calling db.set.error.bypass.on() is a programming error and results in a fatal error.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2010.

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
