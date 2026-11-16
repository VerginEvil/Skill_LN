# cmf.setAppointmentBusystatus()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setappointmentbusystatus( long apid, enum busystatus )`

## Description
Sets the busystatus of the appointment identified by *apid* to the value *busystatus.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `enum` | `busystatus` |  The busy status of the appointment. "BUSY" | "FREE" | "OUTOFOFFICE" | "TENTATIVE"  |

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
