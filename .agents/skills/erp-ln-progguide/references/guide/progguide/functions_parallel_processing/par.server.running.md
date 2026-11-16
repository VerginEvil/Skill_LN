# par.server.running()

## Syntax:
`function boolean par.server.running( )`

## Description
This function will return whether the current session is running in parallel processing server mode. It will be true when function [par.init.server.to.client()](par.init.server.to.client.md) was called successfully. This function can be useful in DLL’s.

## Return values
| | |
|---|---|
| true | Session is running in parallel processing server mode |
| false | Session is not running a parallel processing server mode |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
