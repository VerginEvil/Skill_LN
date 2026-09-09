# enable.commands()

## Syntax:
`function void enable.commands( const string command, const string... )`

## Description
This enables the specified standard and/or form command(s). Standard commands are identified by their [Standard commands](../4gl_features/4gl_choice_sections.md#standard_commands). Form commands are identified either by a function name, a session code, or a menu code.
Because the information is not available, you cannot use this function in the before.program or after.form.read section.

## Arguments
| | | |
|---|---|---|
| `const string` | `command` |  Standard and/or form command(s). Standard commands are identified by their commandIDs. Form commands are identified either by a function name, a session code, or a menu code.  |
| `const string` | `...` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Notes  The [4GL engine](../glossary/glossary.md#fourgl_engine) can enable and disable form commands depending on the number of occurrences currently selected in the form.
You cannot use *enable.commands()* to enable commands that have been disabled either in the form definition or because the user is not authorized for the commands.
Because the information is not yet there, you can not use this function in the before.program section.

## Example
```

enable.commands( "test.function", "ttadv3500m000", ADD.SET )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
