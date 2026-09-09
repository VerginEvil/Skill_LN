# blue.component(), green.component(), red.component()

## Syntax:
`function long blue.component( long color )`
`function long green.component( long color )`
`function long red.component( long color )`

## Description
These return the values of the blue, green, and red components respectively of an rgb color.

## Arguments
| | | |
|---|---|---|
| `long` | `color` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long new_color, red_int, green_int, blue_int
new_color = rgb( 46, 139, 87 )
red_int   = red.component(   new_color )  |  46
green_int = green.component( new_color )  | 139
blue_int  = blue.component(  new_color )  |  87
```

## Related topics
- [Colors overview](overview.md)

- [Colors synopsis](synopsis.md)
