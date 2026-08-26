# current.window()

## Syntax:
`function long current.window( )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This returns the identification number of the current window.
A window becomes current when it is created or when you call [change.window()](change.window.md). All actions to the screen ( *print()* for example) are sent to the current window.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
