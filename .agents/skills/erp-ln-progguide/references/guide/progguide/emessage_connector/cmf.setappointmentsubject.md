# cmf.setAppointmentSubject()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setappointmentsubject( long apid, string subject )`

## Description
Sets the appointment subject of the appointment identified by *apid* to the value *subject.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `string` | `subject` |  The subject of the appointment.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
