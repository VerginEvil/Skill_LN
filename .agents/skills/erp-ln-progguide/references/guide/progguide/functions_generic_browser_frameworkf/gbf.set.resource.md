# gbf.set.resource()

## Syntax:
`#include <bic_gbf>`
`function long gbf.set.resource( long resource.type, void resource.value )`

## Description
This function sets the resources given by resource.type to the given resource.value. The arguments are given in name value pairs.

## Table: Resourcetypes
| | | |
|---|---|---|
| Resource name | Description | GBF default value |
| DsNbackground | background color | default BX input field background color |
| DsNforeground | foreground color | default BX input field foreground color |
| DsNfontSet | font | default BX font |
| DsNheigth | vertical size of the drawing area in pixels | 480 or when the display is smaller than 480 the default is 400 |
| DsNwidth | horizontal size of the drawing area in pixels | 640 or when the display is smaller than 640 the default is 600 |
| DsNtitle | title bar of main window of GBF | Session code (optionally), session description, user name |
| DsNx | horizontal position of the drawing area in pixels | Undetermined |
| DsNy | vertical position of the drawing area in pixels | Undetermined |
| GBF.LINE | color of normal and dashed lines to parent | same as DsNforeground |
| GBF.CYCLE | color of line which indicates cycles | red color (actually the define: RGB.RED) |
| GBF.HSEP | horizontal spacing between vertical line from parent to child icon in pixels | 10 |
| GBF.VSEP | vertical spacing between two consecutive rows (parent to first child, child to next child and so on.) in pixels | 10 |
| GBF.BUTTON | width and height of button | 26 |
For a further explanation about the colors, see text.color in [gbf.add.object()](gbf.add.object.md)
In almost all cases the type will be long (or a domain of basic type int, long, enumerate, bitset and so on.), except when the resource.type is DsNtitle, since in this case the type must be multibyte string.
Note that since Baan V the resource GBF.BUTTON is no longer valid, that is it is not possible to change the value. When this resource is obtained through the [gbf.get.resource()](gbf.get.resource.md) then always the default value will be returned for backward compatibility reasons.

## Arguments
| | | |
|---|---|---|
| `long` | `resource.type` |  The resource type of which to set the value.  |
| `void` | `resource.value` |  The value for the resource type.  |

## Return values
| | |
|---|---|
| 0 | Successful completion |
| GBF.ILL.RESOURCE. TYPE | Unknown resource type specified |
| GBF.ILL.RESOURCE. VALUE | Value for given resource type is not valid |
| GBF.ILL.STATE | GBF is not in the right state to deal with this function |

- [gbf.get.resource()](gbf.get.resource.md)

- [Generic Browser Framework (GBF) overview](overview.md)

- [Generic Browser Framework (GBF) synopsis](synopsis.md)

- [Typical usage](typical_usage.md)

- [Getting started](getting_started.md)

- [Example](example.md)

- [Generic Browser Framework error codes and return values](error_codes_and_return_values.md)

- [standard menu items and function keys](standard_menu_items_and_function_keys.md)

- [Messages and questions](messages_and_questions.md)

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
