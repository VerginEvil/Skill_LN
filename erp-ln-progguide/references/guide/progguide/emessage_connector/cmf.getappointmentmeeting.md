# cmf.getAppointmentMeeting()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getAppointmentMeeting( long apid, ref enum meeting )`

## Description
Gets the meeting flag of the appointment identified by *apid* and returns it in the string *meeting.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `ref enum` | `meeting` |  Appointment meeting: "YES" | "NO"  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object or element not present. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
