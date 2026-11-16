# fieldbutton.align.left()

## Syntax:
`function void fieldbutton.align.left( const string i.command )`

## Description
Tells that the field button should be displayed aligned to the left with the other fields. The field that the field button is connected to will not occupy any space on the form.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.command` |  Form commands are identified either by a function name or a session code.  |

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
- [GenAI Functionality on Form](overview_and_synopsis.md)
