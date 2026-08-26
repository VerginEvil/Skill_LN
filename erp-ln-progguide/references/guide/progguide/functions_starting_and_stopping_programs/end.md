# end()

## Syntax:
`function void end( )`

## Description
When used in a 3GL script, this ends the program and returns control to the application. The database is not updated.
When used in a 4GL script, the function has the same effect as the *end.program* standard command. When a 4GL script calls *end()* or execute(end.program), changes are stored in the database and the program ends. Before the program ends, any [before.choice](../4gl_features/4gl_choice_sections.md) subsections in a [choice.end.program](../4gl_features/4gl_choice_sections.md) section are executed. The [after.program](../4gl_features/4gl_program_sections.md) section is also executed, if present.

## Context
This function is implemented in the 4GL Tools and can be used in 4GL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:
- TIVLevel >= 2120 and In a not trusted process    Note  The functions *end()*, [stop()](stop.md), and [exit()](exit.md) (without an *exitvalue* argument) in 3GL programs, and the function *stop()* in 4GL programs, all have the same effect. That is, the program ends and returns control to the application. The database is not updated.

## Related topics
- [Starting and stopping programs: overview and synopsis](overview_and_synopsis.md)
