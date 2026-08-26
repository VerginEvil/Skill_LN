# cps.status.mess()

## Syntax:
`function void cps.status.mess( const string message )`

## Description
This function displays the specified message in the status bar of a composite session. To clear this message, an empty message string must be passed. This function can be called from composite child sessions (GBF or 4GL). When this function is called from other session types, it will do nothing.

## Arguments
| | | |
|---|---|---|
| `const string` | `message` |  The the message to be shown in the composite status bar  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Composite Sessions overview](overview.md)
- [Composite Sessions synopsis](synopsis.md)
- [Composite Sessions Code Examples](examples.md)
