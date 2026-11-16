# synchronize.satellite()

## Syntax:
`function void synchronize.satellite( const string [satelliteSessionCode]* )`

## Description
Calling this function triggers a synchronization between the header and the active satellite. Since the controller does not know which satellite is currently active, the optional argument is used to indicate for which satellites a synchronization is needed. If the active satellite is not one of the specified satellites, no synchronization is performed. If no arguments are passed a synchronization is performed regardless of which satellite is active.

## Arguments
| | | |
|---|---|---|
| `const string` | `[satelliteSessionCode]*` |  The session codes of the satellites that should be synchronized, separated by commas.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Related topics
- [add.sync.fields()](add.sync.fields.md)

- [add.sync.fields.nokey()](add.sync.fields.nokey.md)

- [add.sync.fields.once()](add.sync.fields.once.md)

- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
