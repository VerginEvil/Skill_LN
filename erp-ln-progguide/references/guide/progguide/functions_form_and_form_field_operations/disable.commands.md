# disable.commands()

## Syntax:
`function void disable.commands( const string command, const string... )`

## Description
This disables the specified standard and/or form command(s). Standard commands are identified by their [Standard commands](../4gl_features/4gl_choice_sections.md#standard_commands). Form commands are identified either by a function name, a session code, or a menu code.

## Arguments
| | | |
|---|---|---|
| `const string` | `command` |  Standard and/or form command(s). Standard commands are identified by their commandIDs. Form commands are identified either by a function name, a session code, or a menu code.  |
| `const string` | `...` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  The [4GL engine](../glossary/glossary.md#fourgl_engine) can enable and disable form commands depending on the number of occurrences currently selected in the form.
Because the information is not available, you can not use this function in the before.program section.

## Example
```

disable.commands( "test.function", "ttadv3500m000", ADD.SET )
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
