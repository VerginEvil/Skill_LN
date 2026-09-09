# chm.next.set.out()

## Syntax:
`function long chm.next.set.out( string set_name(16), ref long element_number, ref string element_name() )`

## Description
*Deprecated.* This function is only supported for Baan Windows and its usage is therefore deprecated.
Use [chm.first.set.out()](chm.first.set.out.md) to retrieve information about the first element in a specified set. Use *chm.next.set.out()* to retrieve information about the next element in the set. To retrieve information about all subsequent elements in the set, you can place this function in a loop that executes as long as the return value is CHM_OK.

## Arguments
| | | |
|---|---|---|
| `string` | `set_name(16)` |  The name of the set for which you want to retrieve information.  |
| `ref long` | `element_number` |  This returns the number of the next element in the set.  |
| `ref string` | `element_name()` |  This returns the name of the next element in the set.  |

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
