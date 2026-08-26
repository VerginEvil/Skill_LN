# chm.set.in()

## Syntax:
`function long chm.set.in( string set_name(16), ref long element_number, string element_name(80) )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
This adds an element to a specified set.

## Arguments
| | | |
|---|---|---|
| `string` | `set_name(16)` |  The name of the set to which the element is to be added.  |
| `ref long` | `element_number` |  The sequence number of the element within the set.  |
| `string` | `element_name(80)` |  The description of the element.  |

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
