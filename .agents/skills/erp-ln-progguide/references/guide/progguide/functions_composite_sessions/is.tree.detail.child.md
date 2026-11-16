# is.tree.detail.child()

## Syntax:
`function boolean is.tree.detail.child( )`

## Description
This function tells whether the current session is running as part of a Tree-Detail session. This function can be useful when a session can be run in standalone mode and as a child within a Tree-Detail session. This function can be called from a 4GL-Session or from a GBF session.

## Return values
| | |
|---|---|
| true | The session is running as a child of a Tree-Detail session |
| false | Otherwise |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
