# cmf.getAppointmentAlldayevent()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getappointmentalldayevent( long apid, ref enum alldayevent )`

## Description
Gets the alldayevent flag of the appointment identified by *apid* and returns it in the string *alldayevent.*

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `ref enum` | `alldayevent` |  All day event appointment: "YES" | "NO"  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object or element not present. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
