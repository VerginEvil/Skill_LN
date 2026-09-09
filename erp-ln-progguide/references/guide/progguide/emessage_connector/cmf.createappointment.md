# cmf.createAppointment()

## Syntax:
`#include <bic_cmf>`
`function long cmf.createappointment( [ long mid ] )`

## Description
Creates a new Infor LN eMessage Connector appointment object.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mid ]` |  Use these optional arguments to pass a message object identification to which this new appointment object will be attached. When this argument is omitted, the function [cmf.addObjectToMessage()](cmf.addobjecttomessage.md) must be used to attach an appointment object to a message object.  |

## Return values
| | |
|---|---|
| <> 0 | (Bshell wide) unique Infor LN eMessage Connector appointment object id. |
| 0 | Appointment object creation error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
