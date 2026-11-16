# chm.domain.out()

## Syntax:
`function long chm.domain.out( long domain_name, ref long data_type, ref string set_name(), ref string title(), ref string unit_label, ref double from value, ref double to_value, ref double interval, ref string display_format() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This retrieves information from the Business Chart Manager about a specified domain. If the client application modifies the information and saves it to the source table or file, the new information is included the next time the chart is started.

## Arguments
| | | |
|---|---|---|
| `long` | `domain_name` |    |
| `ref long` | `data_type` |    |
| `ref string` | `set_name()` |  When the domain type is CHM_SET, this returns the name of the relevant set. For other domain types, this returns an empty string [""] here.  |
| `ref string` | `title()` |  These return the axis title and the unit of measurement that are displayed in the chart to describe the corresponding axis.  |
| `ref string` | `unit_label` |    |
| `ref double` | `from value` |  These return the start and end values of the domain.  |
| `ref double` | `to_value` |    |
| `ref double` | `interval` |  This returns the interval between domain values.  |
| `ref string` | `display_format()` |  For domains of type CHM_REAL or CHM_INTEGER, this returns the display format. See [edit$()](../functions_formatting_io/edit.md).  |

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
