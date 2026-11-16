# donut.new()

## Syntax:
`function long donut.new( const string i.future.use, const string i.legendpos, boolean i.animate )`

## Description
This function creates a new chart of type Donut.

## Arguments
| | | |
|---|---|---|
| `const string` | `i.future.use` |  Future use, currently not used. Leave empty for future use.  |
| `const string` | `i.legendpos` |  Position the legend of the donut will be displayed. Options: DONUT.LEGENDPOS.STANDARD DONUT.LEGENDPOS.RIGHT DONUT.LEGENDPOS.BOTTOM Default: DONUT.LEGENDPOS.RIGHT  |
| `boolean` | `i.animate` |  Tells whether animation is used to display the segments. Default: True  |

## Return values
| | |
|---|---|
| not 0 | Success, the id of the created donut is returned. This is a xml document. |
| 0 | Failure, xml document could not be created. |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2492.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Donut overview and synopsis](overview_and_synopsis.md)
