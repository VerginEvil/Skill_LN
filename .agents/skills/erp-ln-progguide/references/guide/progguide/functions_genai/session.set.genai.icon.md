# session.set.genai.icon()

## Syntax:
`function long session.set.genai.icon( const string i.GenAI.icon )`

## Description
Tells that the current session should be presented as a GenAI session by the action type of the argument, in the session header title.

## Arguments
| |
|---|
| GENAI.ICON.GENERAL, standard icon without specific action. |
| GENAI.ICON.TRANSLATE |
| GENAI.ICON.TEXT |
| GENAI.ICON.BULLET.LIST |
| GENAI.ICON.NUMBER.LIST |
| GENAI.ICON.EMAIL |
| GENAI.ICON.REPORT |
| GENAI.ICON.EXPENSE.REPORT |
| GENAI.ICON.LEDGER.REPORT |
| GENAI.ICON.NOTES |
| GENAI.ICON.PIE.CHART |
| GENAI.ICON.LINE.CHART |
| GENAI.ICON.BAR.CHART |
| GENAI.ICON.SUMMARIZE |
| GENAI.ICON.SEARCH |

## Return values
| | |
|---|---|
| 0 | Success |
| -2 | Failure, unknown GenAI icon. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2531.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "before.program" section

## Related topics
- [GenAI Functionality on Form](overview_and_synopsis.md)
