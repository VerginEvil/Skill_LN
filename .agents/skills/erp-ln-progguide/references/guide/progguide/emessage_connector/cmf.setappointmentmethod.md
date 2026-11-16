# cmf.setAppointmentMethod()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setAppointmentMethod( long apid, domain ttcmf.mth method )`

## Description
Set the METHOD attribute of the appointment identified by *apid* to the value *method*.

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `domain ttcmf.mth` | `method` |  The new method value, which is one of `ttcmf.mth.request` (for sending a new or update on an appointment) or `ttcmf.mth.cancel` (for canceling an appointment).  |

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
