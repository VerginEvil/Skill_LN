# rsc.get()

## Syntax:
`function void rsc.get( ref string values(), string package_code(2), string resource_set(16), string resource_id(24),... )`

## Description

## Arguments
| | | |
|---|---|---|
| `ref string` | `values()` |  The returned resource values. This argument must be long enough to accommodate the number of requested resources.  |
| `string` | `package_code(2)` |  The package code.  |
| `string` | `resource_set(16)` |  The resource set ID.  |
| `string` | `resource_id(24),...` |  One or more IDs of individual resources.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

long   foreground_color, background_color
string gui_font(80)

foreground_color = RGB.RED
background_color = RGB.WHITE
gui_font = rsc.font.spec( FNTMEDIUM, FNTROMAN, 14, 0,FNTVARIABLE,
140, 0 )

rsc.put( "tt", "desktop", "foreground", rsc.long( foreground_color
),
        "background", rsc.long( background_color ), "font",
                rsc.string( gui_font ) )

rsc.reload()
```

## Related topics
- [Resource sets overview](overview.md)
- [Resource sets synopsis](synopsis.md)
