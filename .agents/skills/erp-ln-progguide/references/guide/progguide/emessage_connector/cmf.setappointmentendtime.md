# cmf.setAppointmentEndtime()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setappointmentendtime( long apid, domain ttutc endtime )`

## Description
Sets the endtime of the appointment identified by *apid* to the value *endtime.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `domain ttutc` | `endtime` |  The end time of the appointment.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object. |
| -2 | Date conversion error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
