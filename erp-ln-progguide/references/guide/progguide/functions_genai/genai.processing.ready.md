# genai.processing.ready()

## Syntax:
`function void genai.processing.ready( )`

## Description
Tells that the processing of the GenAI command is ready. If a User clicks on a GenAI field button, the button will show some animation on the button to let the user know that processing is happening. If this function is called, LN UI will be told with the next reply to LN UI, that the processing is ready and the processing animation can be stopped..

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2496.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function must only be called if a GenAI command is active.

## Related topics
- [GenAI Functionality on Form Overview](overview_and_synopsis.md)
