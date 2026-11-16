# bg$()

## Syntax:
`function string bg$( )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
Use this to set the background color of the current window. The color argument can have the following values:
| | | | |
|---|---|---|---|
| CW.BLACK | CW.BLUE | CW.GREEN | CW.CYAN |
| CW.RED | CW.MAGENTA | CW.YELLOW | CW.WHITE |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

print bg$( CW.RED )
refresh()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
