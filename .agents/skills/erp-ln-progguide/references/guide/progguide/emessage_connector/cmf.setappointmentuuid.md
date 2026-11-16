# cmf.setAppointmentUUID()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setAppointmentUUID( long apid, string uuid )`

## Description
Set the unique identifier attribute of the appointment identified by *apid* to the value *uuid*. The function *cmf.createAppointment()* creates globally unique identifier and assigns it to the created appointment object. The function *cmf.setAppointmentUUID()* can be used to change this identifier. This identifier is used by calendar systems to correlate previously sent appointments to this appointment. For instance to recognize an appointment as an update of previously sent appointment the same UUID must be used. In addition the UUID must be set by the application to cancel a previously sent appointment.

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `string` | `uuid` |  The new uuid value.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
