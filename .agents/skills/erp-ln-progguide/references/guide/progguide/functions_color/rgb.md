# rgb()

## Syntax:
`function long rgb( long red, long green, long blue )`

## Description
Use this to compose a color by specifying its red, green, and blue intensities. The intensities must be in the range 0 to 255.

## Arguments
| | | |
|---|---|---|
| `long` | `red` |    |
| `long` | `green` |    |
| `long` | `blue` |    |

## Return values
A long which can be used as a color in graphical contexts such as windows, user interface controls, and so on.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

long new_color, red_int, green_int, blue_int
                new_color = rgb(46,139,87)
                red_int = red.component( new_color )            |
46
                green_int = green.component( new_color )        |
139
                blue_int = blue.component( new_color )  | 87
```

## Related topics
- [Colors overview](overview.md)

- [Colors synopsis](synopsis.md)
