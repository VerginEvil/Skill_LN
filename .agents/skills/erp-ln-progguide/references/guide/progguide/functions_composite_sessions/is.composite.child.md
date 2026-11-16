# is.composite.child()

## Syntax:
`function boolean is.composite.child( )`

## Description
This function checks whether the current session is running as a composite child session or not. This function can be useful when a session can be run in standalone mode and as a child within a composite session. This function can be called from a 4GL-Session or from a GBF session.

## Return values
| | |
|---|---|
| true | this session is running as a composite child session |
| false | otherwise |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
