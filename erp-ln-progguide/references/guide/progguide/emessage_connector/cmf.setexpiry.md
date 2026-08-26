# cmf.setExpiry()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setexpiry( long mid, domain ttutc expiry )`

## Description
Sets the expiry time of the message identified by *mid* to the value *expiry.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `domain ttutc` | `expiry` |  Message expiry time.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object. |
| -2 | Date conversion error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
