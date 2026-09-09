# chm.domain.in()

## Syntax:
`function long chm.domain.in( long domain_name, long data_type, string set_name(16), string title(16), string unit_label(16), double from_value, double to_value, double interval, string display_format(80) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This defines a domain, which specifies a start value, an end value, and a step value for a particular axis. The domain determines which values are legal for the axis.

## Arguments
| | | |
|---|---|---|
| `long` | `domain_name` |  This specifies the name of the domain. The possible values are: CHM_SERIES_DOMAIN CHM_CATEGORY_DOMAIN CHM_DATA_DOMAIN CHM_DATA2_DOMAIN  |
| `long` | `data_type` |  This specifies the domain type. The possible values are: CHM_REAL real (the domain consists of integers and fractions) CHM_INTEGER integer (the domain consists of integers) CHM_SET enumerated set (the domain consists of a set of labels)  |
| `string` | `set_name(16)` |  When the domain type is CHM_SET, this specifies the name of the relevant set. For other domain types, specify an empty string [""] here. Use [chm.set.in()](chm.set.in.md) to define the set.  |
| `string` | `title(16)` |  These specify the axis title and the unit of measurement that must be displayed in the chart to describe the corresponding axis.  |
| `string` | `unit_label(16)` |    |
| `double` | `from_value` |  These specify the start and end values of the domain. You can calculate these values with the function [chm.scale.axis()](chm.scale.axis.md).  |
| `double` | `to_value` |    |
| `double` | `interval` |  This specifies the interval between domain values.  |
| `string` | `display_format(80)` |  For domains of type CHM_REAL or CHM_INTEGER, you must specify a display format. See [edit$()](../functions_formatting_io/edit.md).  |

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
