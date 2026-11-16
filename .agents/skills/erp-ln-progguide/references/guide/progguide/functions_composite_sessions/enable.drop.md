# enable.drop()

## Syntax:
`function void enable.drop( const string session.code, const string on.drop.function )`

## Description
Allow drop operation onto this 4GL-Session from objects dragged from the indicated sessions. When an object from the indicated session is dropped, the function passed in string *on.drop.function* will be called. This function can be called more than once in order to allow drop operations from different sessions. This function must be called from the *before.program:* section or from the *after.form.read:* section of a multi-occurrence 4GL-Session which runs as a composite child.

## Arguments
| | | |
|---|---|---|
| `const string` | `session.code` |  Code of the session from which objects can be dropped  |
| `const string` | `on.drop.function` |  The name of the function that will be called when a drop event occurs. This function must be declared as described here: [on.drop()](on.drop.md).  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Related topics
- [Composite Sessions overview](overview.md)

- [Composite Sessions synopsis](synopsis.md)

- [Composite Sessions Code Examples](examples.md)
