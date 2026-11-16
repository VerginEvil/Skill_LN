# cmf.isServiceEnabled()

## Syntax:
`#include <bic_cmf>`
`function long cmf.isserviceenabled( domain ttcmf.prov service )`

## Description
Checks in the Services (ttcmf030) table if service is enabled (ttcmf030.enab = yes) or not.

## Arguments
| | | |
|---|---|---|
| `domain ttcmf.prov` | `service` |  The service identification.  |

## Return values
| | |
|---|---|
| 1 | true: service is enabled |
| 0 | false: service is disabled. |
| -1 | service not found in table Services (ttcmf030) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
