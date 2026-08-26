# execute()

## Syntax:
`function void execute( long command )`

## Description
This executes the specified standard command. Normally, standard commands are activated by the user. This function enables applications to execute standard commands without user intervention. This is useful, for example, if you want to display the first record of the main table when a session is started.
Infinite recursion is possible when using this command. For example, if you include execute(add.set) in the *after.choice* subsection of *choice.add.set*. So, never use this function to execute a standard command in its own choice sections.

## Arguments
| | | |
|---|---|---|
| `long` | `command` |   |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
Note  For a list of all standard commands and the program types in which you can use them, see Standard commands.

## Example
```

form.2:
init.form:
    execute( first.set )
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
