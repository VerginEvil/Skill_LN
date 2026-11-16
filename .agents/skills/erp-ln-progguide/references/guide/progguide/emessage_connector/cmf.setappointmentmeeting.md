# cmf.setAppointmentMeeting()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setappointmentmeeting( long apid, enum meeting )`

## Description
Sets the meeting flag of the appointment identified by *apid* to the value *meeting.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `enum` | `meeting` |  Appointment meeting: "YES" | "NO"  |

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
