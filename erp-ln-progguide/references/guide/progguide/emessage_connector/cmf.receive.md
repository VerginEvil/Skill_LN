# cmf.receive()

## Syntax:
`#include <bic_cmf>`
`function long cmf.receive( long mid, domain ttcmf.prov service, long block )`

## Description
Receives a Infor LN eMessage Connector message object and returns the object id in *mid*. The appropriate connector must have been previously started prior to calling this function using cmf.startService()cmf.startService .

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `domain ttcmf.prov` | `service` |  Service offered by a provider, for example, Fax or Email.  |
| `long` | `block` |  Flag indicating whether cmf.receive will wait for a message (blocking) or simply return if there is no message waiting (nonblocking).  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error receiving message. |
| -2 | Service not started. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
