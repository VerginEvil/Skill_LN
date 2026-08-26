# par.server.id()

## Syntax:
`function long par.server.id( )`

## Description
This function will return the identification of a server within its group. This function can be useful in includes or DLL’s to determine if the session is running in the context of parallel processing.

## Return values
| | |
|---|---|
| > 0 | The server number when the session is running in a parallel processing context |
| 0 | Session is not running a parallel processing context |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)
- [Parallel Application Processing synopsis](synopsis.md)
- [Parallel Application Processing Examples](examples.md)
