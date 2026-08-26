# cmf.getChargeCode()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getchargecode( long mid, ref string chargecode )`

## Description
Gets the message charge code of the message identified by *mid* and returns string into *chargecode.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref string` | `chargecode` |  Message charge code.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id or element not present).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
