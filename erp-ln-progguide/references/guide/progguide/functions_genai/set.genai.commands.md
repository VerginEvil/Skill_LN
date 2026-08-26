# set.genai.commands()

## Syntax:
`function void set.genai.commands( const string i.command, [ const string ... ] )`

## Description
Tells that the command named in the argument should be represented as a GenAI option.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.command` |  Form commands are identified either by a function name or a session code.  |
| `[ const string` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Command not found. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2496.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "after.form.read" section

## Related topics
- [GenAI Functionality on Form Overview](overview_and_synopsis.md)
