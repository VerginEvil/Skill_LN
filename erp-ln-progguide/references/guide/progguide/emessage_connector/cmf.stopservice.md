# cmf.stopService()

## Syntax:
`#include <bic_cmf>`
`function long cmf.stopservice( long service(15), long mode )`

## Description
Stops the currently running Infor LN eMessage Connector service named *service* which is running in mode *mode.*

## Arguments
| | | |
|---|---|---|
| `long` | `service(15)` |    |
| `long` | `mode` |    |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | No service running. |
| -2 | Service could not be stopped normally. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
