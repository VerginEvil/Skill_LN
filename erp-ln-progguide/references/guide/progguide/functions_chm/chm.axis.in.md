# chm.axis.in()

## Syntax:
`function long chm.axis.in( long axis_name, long logarithmic, long log_base, long divisions, double divisionstep, double intersection, string division_set(16) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This defines an axis for an axis-oriented graph.

## Arguments
| | | |
|---|---|---|
| `long` | `axis_name` |  |
| `long` | `logarithmic` |  If logarithmic scaling is required, set this to true. For linear scaling, set it to false.  |
| `long` | `log_base` |  For logarithmic scaling, this indicates the log base that must be used. The argument is ignored if *logarithmic* is set to false.  |
| `long` | `divisions` |  |
| `double` | `divisionstep` |  This specifies the interval between two divisions on the axis. You can use [chm.scale.axis()](chm.scale.axis.md) to calculate the division step.  |
| `double` | `intersection` |  This indicates the value on the data axis where the category and data axes intersect.  |
| `string` | `division_set(16)` |  Normally, the values or labels from the associated domain are displayed on the axis. You can override this by specifying the name of a different set here. You create the set with [chm.set.in()](chm.set.in.md).  |

## Return values
| | |
|---|---|
| CHM_OK | Success. |
| CHM_ERROR | Error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Chart manager overview](overview.md)
- [Chart manager synopsis](synopsis.md)
- [Creating a chart manager client application](creating_a_chart_manager_client_application.md)
- [Chart manager example](example.md)
