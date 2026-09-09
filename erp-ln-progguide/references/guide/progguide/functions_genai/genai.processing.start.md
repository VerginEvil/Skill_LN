# genai.processing.start()

## Syntax:
`function void genai.processing.start( )`

## Description
Tells the session that GenAI processing will be started. If a form field on the session has been set as being a GenAI field showing process animation by function set.GenAI.field, a AI-process animation will be displayed in the field. GenAI processing will continue until the current action, i.e the start of the session, is finished or the function GenAI.processing.ready is called.

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Failure, session is not as being a GenAI session. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2590.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function should be called in the "init.group" of group 1 section if the GenAI processing is started during the start of the session. Or in any command section, if the GenAI processing is triggered by an option on the session.

## Related topics
- [GenAI Functionality on Form](overview_and_synopsis.md)
