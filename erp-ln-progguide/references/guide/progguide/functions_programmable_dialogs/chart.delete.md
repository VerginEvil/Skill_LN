# chart.delete()

## Syntax:
`#include <bic_dialog>`
`function long chart.delete( long type )`

## Description
Deletes the XML Document of the chart.
Note that this function only effects the *LN UI* User Interface.
Note that this function can only be used for fields of type *Picture*. Currently this type can only be defined by an Session Extension.

## Arguments
| | | |
|---|---|---|
| `long` | `type` |  The identifier of the chart. The identifier must be returned by the function chart.new()  |

## Return values
| | |
|---|---|
| 0 | Success. |
| <>0 | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2320.

## Related topics
- [chart.new()](chart.new.md)

- [Programmable dialogs synopsis](synopsis.md)

- [Example chart](examplechart.md)
