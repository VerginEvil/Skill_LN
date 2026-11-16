# chart.write()

## Syntax:
`#include <bic_dialog>`
`function long chart.write( long type, string file, long width, long height )`

## Description
Creates a picture for the given chart.
Note that this function only effects the *LN UI* User Interface.
Note that this function can only be used for fields of type *Picture*. Currently this type can only be defined by an Session Extension.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  The identifier of the chart. The identifier must be returned by the function chart.new()  |
| `string` | `file` |  Name of the file, including path, to which the picture should be written.  |
| `long` | `width` |  The width in pixels of the picture.  |
| `long` | `height` |  The height in pixels of the picture.  |

## Return values
Result of the creation of the picture.
| | |
|---|---|
| 0 | Success. |
| -1 - -4 | JavaVM error. To create the picture from the chart xml document a java method is called. This call returned an error. |
| -10 | No chart xml document was given. |
| -20 | The type of the chart is not set or not supported. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2320.

## Related topics
- [chart.new()](chart.new.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
