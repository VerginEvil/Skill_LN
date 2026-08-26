# rsc.put()

## Syntax:
`function void rsc.put( string package_code(2), string resource_set(16), string resource_id(16), value(40) , [ string resource_id(16), value(40) . . . ] )`

## Description
This updates one or more resource values in a specified resource set. You can use the following functions to convert program variables to a resource value format: [rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()](rsc.many.md), [rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()](rsc.many.md), [rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()](rsc.many.md), [rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()](rsc.many.md), and [rsc.boolean(), rsc.double(), rsc.enum(), rsc.long(), rsc.string()](rsc.many.md).

## Arguments
| | | |
|---|---|---|
| `string` | `package_code(2)` |  The package code.  |
| `string` | `resource_set(16)` |  The resource set ID.  |
| `string` | `resource_id(16), value(40)` |  One or more name/value pairs. Each pair consists of the ID of a resource that must be updated and the new value for that resource.  |
| `[ string` | `resource_id(16), value(40) . . . ]` |  One or more name/value pairs. Each pair consists of the ID of a resource that must be updated and the new value for that resource.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
long foreground_color, background_color
string gui_font(80)
foreground_color = RGB.RED
background_color = RGB.WHITE
gui_font = rsc.font.spec( FNTMEDIUM, FNTROMAN, 14, 0,FNTVARIABLE, 140, 0 )
rsc.put( "tt", "desktop", "foreground", rsc.long( foreground_color ),
"background", rsc.long( background_color ), "font",
rsc.string( gui_font ) )
rsc.reload()

## Related topics
- [Resource sets overview](overview.md)
- [Resource sets synopsis](synopsis.md)
