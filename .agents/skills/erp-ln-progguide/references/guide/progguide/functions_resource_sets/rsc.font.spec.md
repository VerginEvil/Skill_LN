# rsc.font.spec()

## Syntax:
`function string rsc.font.spec( long font_weight, long font_slant, long font_height, long font_points, long font_spacing, long font_width, long font_charwidth )`

## Description
This returns a string that defines a font with the specified characteristics.

## Arguments
| | | |
|---|---|---|
| `long` | `font_weight` |  The font width. Possible values are: FNTMEDIUM, FNTBOLD or FNTNORMAL.  |
| `long` | `font_slant` |  The font slant. Possible values are: FNTROMAN or FNTITALIC.  |
| `long` | `font_height` |  The font height in pixels.  |
| `long` | `font_points` |  The font height in tenths of a point (a point is 1/72th of an inch).  |
| `long` | `font_spacing` |  The type of spacing. Possible values are: FNTFIXED or FNTVARIABLE.  |
| `long` | `font_width` |  The average width of the font, in tenths of a pixel.  |
| `long` | `font_charwidth` |  The average character width, in pixels. This overides the *font_width* value.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Return value
A string that defines a font with the specified characteristics.

## Example
See [rsc.put()](rsc.put.md).

## Related topics
- [Resource sets overview](overview.md)

- [Resource sets synopsis](synopsis.md)
