# stop()

## Syntax:
`function void stop( )`

## Description
This ends the program. The program immediately exits without updating the database and without executing any further sections. The function has the same effect in both 3GL and 4GL scripts.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process    Note  The functions [end()](end.md), *stop()*, and [exit()](exit.md) (without an *exitvalue* argument) in 3GL programs, and the function *stop()* in 4GL programs, all have the same effect. That is, the program ends and returns control to the application. The database is not updated.

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
