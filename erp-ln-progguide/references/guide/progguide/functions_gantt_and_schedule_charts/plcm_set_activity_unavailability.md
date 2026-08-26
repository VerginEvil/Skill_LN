# plcm.set.activity.unavailability

## Syntax:
`function long plcm.set.activity.unavailability( const string activity.id(), const long no.elements, const long start.date(), const long end.date(), const string description() mb, const string legend.id() mb )`

## Description
Sets the unavailabilities of an activity. This show the bars of unavailabilities on the background of the row of the activity and provide an insight of the availability of the activity.
The background display can be dis-/enabled with the button "Show Availability".

## Arguments
| | | |
|---|---|---|
| `const string` | `activity.id()` |  Unique ID of the referenced activity.  |
| `const long` | `no.elements` |  Number of unavailabilities of the activity  |
| `const long` | `start.date()` |  Array of start dates of the unavailability. (no.elements occurrences)  |
| `const long` | `end.date()` |  Array of end dates of the unavailability. (no.elements occurrences)  |
| `const string` | `description() mb` |  Array of descriptions of the unavailability. (no.elements occurrences)  |
| `const string` | `legend.id() mb` |  Array of legend ID’s of the unavailability. (no.elements occurrences)  |

## Return values
| | |
|---|---|
| 0 | Success |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function is available from [Tools Interface Version (TIV)](../tiv/tiv_overview.md) [TIV 2140](../tiv/tiv_2140.md) and requires LN UI 12.0.4 or higher.

## Related topics
- [Synopsis](synopsis.md)
- [plcm.get.default.availability](plcm_get_activity_unavailability.md)
