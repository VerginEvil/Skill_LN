# chm.axis.out()

## Syntax:
`function long chm.axis.out( long axis_name, ref long logarithmic, ref long log_base, ref long divisions, ref double divisionstep, ref double intersection, ref string division_set() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information about a specified axis from the Business Chart Manager. If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.

## Arguments
| | | |
|---|---|---|
| `long` | `axis_name` |    |
| `ref long` | `logarithmic` |  This returns true if the axis uses logarithmic scaling, or false if it uses linear scaling.  |
| `ref long` | `log_base` |  If *logarithmic* returns true, this argument returns the log base used.  |
| `ref long` | `divisions` |  This returns the number of divisions into which the axis is divided.  |
| `ref double` | `divisionstep` |  This returns the interval between two divisions on the axis.  |
| `ref double` | `intersection` |  This returns the value on the data axis where the category and data axes intersect.  |
| `ref string` | `division_set()` |  If the labels or values displayed on the axis are provided by a set created by [chm.set.in()](chm.set.in.md) instead of by the domain associated with the axis, this argument returns the name of the set used.  |

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
