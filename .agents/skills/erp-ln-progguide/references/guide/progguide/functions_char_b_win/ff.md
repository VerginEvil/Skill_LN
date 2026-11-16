# ff$()

## Syntax:
`function string ff$( )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to send a form feed to the printer. The result of this function cannot be sent to the screen.

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

spool.pr.line = ff$()
spool.line()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
