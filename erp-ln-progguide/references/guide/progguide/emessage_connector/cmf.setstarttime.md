# cmf.setStartTime()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setstarttime( long mid, domain ttutc starttime )`

## Description
Sets the delivery start time of the message identified by *mid* to the value *starttime.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `domain ttutc` | `starttime` |  Start time when the message must be delivered.  |

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
