# cmf.send()

## Syntax:
`#include <bic_cmf>`
`function long cmf.send( long mid, string service(15) )`

## Description
Sends the Infor LN eMessage Connector message object identified by *mid* using the service specified by *service*. The message class is set to the service name.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `string` | `service(15)` |  Service offered by a provider, for example, Fax or Email.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error sending message |
| -2 | Service not started |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
