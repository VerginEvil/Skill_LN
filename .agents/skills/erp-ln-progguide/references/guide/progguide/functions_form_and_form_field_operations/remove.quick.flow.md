# remove.quick.flow()

## Syntax:
`function void remove.quick.flow( const string frmcmd, const string... )`

## Description
This function can be used in the after.form.read section to remove the quick.flow support for one or more form commands. In this way the application script can decide to not support quick.flow based on a paremaeter.

## Arguments
| | | |
|---|---|---|
| `const string` | `frmcmd` |  Form command(s). Form commands are identified either by a function name, a session code, or a menu code.  |
| `const string` | `...` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

remove.quick.flow( "ttadv3500m000" )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
