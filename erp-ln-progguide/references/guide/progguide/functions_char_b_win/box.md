# box()

## Syntax:
`function void box( long box_x, long box_y, long box_width, long box_height, long mode )`

## Description
*Deprecated.* This function is only supported for character-based windows and its usage is therefore deprecated.
This draws a rectangle on the screen. If the specified box does not fit in the current window, only the part that does fit is displayed.
Changes become visible on screen only after calling [refresh()](refresh.md).

## Arguments
| | | |
|---|---|---|
| `long` | `box_x` |  The screen co-ordinates for the top left corner of the box.  |
| `long` | `box_y` |    |
| `long` | `box_width` |  The width and height respectively of the box.  |
| `long` | `box_height` |    |
| `long` | `mode` |  0 only the box is drawn; no other screen modifications are made 1 the interior of the box is cleared 2 the box is drawn dimmed; no other screen modifications are made 3 the box is drawn dimmed and its interior is cleared In addition to the above values, you can specify special effects such as reversed and blinking. For a list of possible attributes, see see [cf$()](cf.md).  |

## Context
This function is implemented in the porting set and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Examples
```

| This draws the largest possible box
box( 1, 1, 80, 23, mode )
refresh()
| This draws a box with the reverse attribute
cf_mode = 41      | attribute 4 (* 10) + mode 1
box( 2, 2, 40, 13, cf_mode )
refresh()
```

## Related topics
- [Character-based windows - overview and synopsis](overview_and_synopsis.md)
