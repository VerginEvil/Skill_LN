# cmf.setRecipientResponsibility()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setrecipientresponsibility( long recipient, string responsibility )`

## Description
Sets the responsibility of the recipient identified by *recipient* to the value *responsibility.*

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `string` | `responsibility` |  The responsibility of the recipient: "TRUE"|"FALSE"  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid recipient id. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
