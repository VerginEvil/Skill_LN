# dal.clear.error.messages()

## Syntax:
`function void dal.clear.error.messages( )`

## Description
This clears all DAL error messages from the message buffer. Abbreviation for dal.reset.error.messages(0).

## Context
This function is implemented in the 4GL Tools and can be used in DAL script types.
This function is marked as 'conditionally trusted' and can therefore only be used in trusted objects or 'conditionally' in not trusted objects. More about trusted and not trusted objects can be found in the section about [managed execution.](../misc/managed_execution.md).
In the following case it is possible to use this function in a not trusted object:

- TIVLevel >= 2120 and In a not trusted process

## Related topics
- [Message handling overview and synopsis](overview_and_synopsis.md)
