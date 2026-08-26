# cmf.enableService()

## Syntax:
`#include <bic_cmf>`
`function long cmf.enableservice( domain ttcmf.prov service, long enable )`

## Description
Checks in the Services (ttcmf030) table if service is enabled (ttcmf030.enab = yes) or not. If not, and enable is true, then service is enabled. If yes, and enable is false, then service is disabled. In the other (two) cases nothing happens.

## Arguments
| | | |
|---|---|---|
| `domain ttcmf.prov` | `service` |  The service identification.  |
| `long` | `enable` |  |

## Return values
| | |
|---|---|
| 2 | service is enabled. |
| 1 | service is disabled. |
| 0 | nothing changed. |
| -1 | service not found in table Services (ttcmf030).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
