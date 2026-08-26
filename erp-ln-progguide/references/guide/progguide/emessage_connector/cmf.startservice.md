# cmf.startService()

## Syntax:
`#include <bic_cmf>`
`function long cmf.startservice( long service(15), long mode, [ string address(13) ] )`

## Description
Starts the Infor LN eMessage Connector service

## Arguments
| | | |
|---|---|---|
| `long` | `service(15)` |  The service offered by a provider, for example, Fax or Email.  |
| `long` | `mode` |  Mode the connector should start in. 1 = Inbound 2 = Outbound  |
| `[ string` | `address(13) ]` |  An alternate name to the default that the connector should connect to the external service. It replaces the session code in the address the connector uses, e.g. `ttcmfnotify.000.saturn` becomes `anyname.000.saturn.`  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Service not present. |
| -2 | Service could not be started. |
| -3 | Service not enabled. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
