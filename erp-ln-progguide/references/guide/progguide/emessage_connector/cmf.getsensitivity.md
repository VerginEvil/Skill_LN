# cmf.getSensitivity()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getsensitivity( long mid, ref enum sensitivity )`

## Description
Gets the sensitivity of the message identified by *mid* and returns it in the enum *sensitivity*.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref enum` | `sensitivity` |  Message sensitivity. “NORMAL” | “PERSONAL” | “PRIVATE” | “CONFIDENTIAL” | “SECRET”  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object or element not present. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
