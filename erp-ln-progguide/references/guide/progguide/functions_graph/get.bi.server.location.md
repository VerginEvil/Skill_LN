# get.bi.server.location()

## Syntax:
`function string get.bi.server.location( )`

## Description
This function returns the location of the BI Server linked to the current package combination. If the current package combination has no specific BI server linked to it, the function returns the BI server that is not linked to any package combination.

## Return values
| | |
|---|---|
| filled | URL of the BI Server. |
| empty | If BI Server not configured. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Graph on Form Overview](overview.md)
- [Graph on Form synopsis](synopsis.md)
