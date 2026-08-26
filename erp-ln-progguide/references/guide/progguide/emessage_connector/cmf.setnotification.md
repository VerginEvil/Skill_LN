# cmf.setNotification()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setnotification( long mid, enum notification )`

## Description
Sets the notification required of the message identified by *mid* to the value *notification.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `enum` | `notification` |  Message Notification: "ALWAYS"|"DELIVERY"|"NON-DELIVERY"|"NEVER"  |

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
