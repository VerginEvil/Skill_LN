# cmf.setAppointmentDescription()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setAppointmentDescription( long apid, string description )`

## Description
Set the description text of the appointment identified by *apid* to the value *description*. The description of an appointment is optional and may consist of multiple lines of text. Each line must be terminated by a linefeed character.

## Arguments
| | | |
|---|---|---|
| `long` | `apid` |  The appointment identification.  |
| `string` | `description` |  The description text.  |

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
