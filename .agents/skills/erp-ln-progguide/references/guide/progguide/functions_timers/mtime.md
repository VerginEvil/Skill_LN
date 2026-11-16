# mtime()

## Syntax:
`function long mtime( )`

## Description
This measures the time elapsed since the first *mtime()* call. The function is common to all processes within the same bshell. That is, when it is called by a process, the result is the number of milliseconds since the function was first called by a process in the same bshell.

## Return values
The first call returns 0. Subsequent calls return the number of milliseconds since the first call. A negative value is returned if an error occurs.

## Context
This function is implemented in the porting set and can be used in all script types.
Note  The maximum time frame that *mtime()* can measure is 2147483647 milliseconds (approximately 596 hours).

## Related topics
- [Timers overview and synopsis](overview_and_synopsis.md)
