# par.get.no.of.server()

## Syntax:
`function long par.get.no.of.server( )`

## Description
This function will return the number of servers configured for this client session. See the section [Parallel Application Processing Configuration](configuration.md).

## Return values
| | |
|---|---|
| > 0 | number of servers configured for this client session |
| <= 0 | session not configured for parallel processing operation |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2400

## Related topics
- [Parallel Application Processing Overview](overview.md)

- [Parallel Application Processing synopsis](synopsis.md)

- [Parallel Application Processing Examples](examples.md)
