# add.sync.fields.nokey()

## Syntax:
`function void add.sync.fields.nokey( const string satelliteSessionCode, const string ... )`

## Description
This function maps a variable in the multi-main table controller session to a variable in the session. Both of these variables must be declared as external.
This variable can then be used in the satellite session, for example in a query.extend to add more complex conditions
This function is relevant in multi-main table controller sessions only.

## Arguments
| | | |
|---|---|---|
| `const string` | `satelliteSessionCode` |  The session code of the satellite.  |
| `const string` | `...` |  Pairs of arguments of the form [const string controllerVariableName, const string satelliteVariableName].  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Notes  This function can only be used in the after.form.read() section of the program script.

## Related topics
- [add.sync.fields()](add.sync.fields.md)
- [add.sync.fields.once()](add.sync.fields.once.md)
- [synchronize.satellite()](synchronize.satellite.md)
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
