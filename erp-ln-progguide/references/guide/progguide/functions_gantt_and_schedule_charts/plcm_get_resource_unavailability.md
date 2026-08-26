# plcm.get.resource.unavailability

## Syntax:
`function void plcm.get.resource.unavailability( const string resource.id(), const long i.start.date, const long i.end.date )`

## Description
Callback-function when the scope of the view of unavailabilities of the resource is changed in the UI.

## Arguments
| | | |
|---|---|---|
| `const string` | `resource.id()` |  Unique ID of the referenced resource.  |
| `const long` | `i.start.date` |  input of the start date of the view for unavailabilities.  |
| `const long` | `i.end.date` |  input of the end date of the view for unavailabilities.  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function can be implemented with [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2140](../tiv/tiv_2140.md) and requires LN UI 12.0.4 or higher.

## Related topics
- [Synopsis](synopsis.md)
- [Example structure availability](example_background.md)
