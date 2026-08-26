# chm.scale.axis()

## Syntax:
`function void chm.scale.axis( double from_value, double to_value, long divisions, double factor, ref double domain_from_value, ref double domain_to_value, ref double divisionstep )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This generates a scaling based on the minimum and maximum data values to be presented by the graph and on the number of divisions required. You can use the returned *domain_from_value*, *domain_to_value*, and *divisionstep* as inputs to [chm.domain.in()](chm.domain.in.md) and [chm.axis.in()](chm.axis.in.md).

## Arguments
| | | |
|---|---|---|
| `double` | `from_value` |  Use these to specify the minimum and maximum data values to be presented by the graph.  |
| `double` | `to_value` |  |
| `long` | `divisions` |  Use this to specify the number of divisions required. The axis will be divided into the specified number of divisions.  |
| `double` | `factor` |  |
| `ref double` | `domain_from_value` |  The function calculates and returns these values, which are the minimum and maximum values of the domain. These will be the start and end points of the axis.  |
| `ref double` | `domain_to_value` |  |
| `ref double` | `divisionstep` |  This returns the size of the steps that separate the divisions on the axis.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
