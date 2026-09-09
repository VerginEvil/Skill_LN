# gbf.start()

## Syntax:
`function long gbf.start( long read.levels, long show.levels )`

## Description
Activates the GBF,in other words it takes over control from the application. See also [gbf.init()](gbf.init.md) for more information.
read.levels
The [gbf.start()](gbf.start.md) function will first try to read the number of levels of the tree as specified with the read.levels argument. If the read.levels argument is not given, it is set to 1. The possibilities for read.levels and the actions are:
| | |
|---|---|
| read.levels | description |
| < 0 | return an error, GBF is not activated |
| GBF.READ.ALL | read all levels |
| 1 | read only top level |
| > 1 | read up to the given number of levels |
It is not considered an error when the specified read.levels cannot be read from the tree, thus when specifying too many levels which are not present in the actual tree.
show.levels
After this the number of levels contained in show.levels is displayed in the window. If the show.levels argument is not given, it is set to the value of read.levels. The possibilities for show.levels and the actions are:
| | |
|---|---|
| show.levels | description |
| < 0 | return an error, GBF is not activated |
| GBF.SHOW.ALL | show all levels which are read |
| <= read.levels | show up to the given number of levels |
| > read.levels | show up to read.levels |
After this the main event loop is activated, effectively meaning that the GBF is now in control.
When the GBF is done it will return to the calling application, returning control to the main application.

## Arguments
| | | |
|---|---|---|
| `long` | `read.levels` |  See above.  |
| `long` | `show.levels` |  See above.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.NO.MEMORY | Not enough memory |
| GBF.ILL.LEVEL | Illegal read.levels or show.levels given |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |
| GBF.CHILD.ABORT | Exited on a child request, see gbf.menu.action() |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Related topics
- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)
