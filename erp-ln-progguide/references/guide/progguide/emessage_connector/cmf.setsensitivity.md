# cmf.setSensitivity()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setsensitivity( long mid, enum sensitivity )`

## Description
Sets the sensitivity of the message identified by *mid* to the value *sensitivity*.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `enum` | `sensitivity` |  Message sensitivity. “NORMAL” | “PERSONAL” | “PRIVATE” | “CONFIDENTIAL” | “SECRET"  |

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
