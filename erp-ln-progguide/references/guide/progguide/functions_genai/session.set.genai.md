# session.set.genai()

## Syntax:
`function void session.set.genai( [ boolean i.show.as.AI.dialog ] )`

## Description
Tells that the current session should be presented as a GenAI session in the session header title.

## Arguments
| | | |
|---|---|---|
| `[ boolean` | `i.show.as.AI.dialog ]` |  True, to show the 4gl dialog as an AI-dialog. Besides the header title additional changes are made to the look of the dialog.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2496.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.program" section. The optional argument i.show.as.dialog is available from TIV level 2590

## Related topics
- [GenAI Functionality on Form](overview_and_synopsis.md)
