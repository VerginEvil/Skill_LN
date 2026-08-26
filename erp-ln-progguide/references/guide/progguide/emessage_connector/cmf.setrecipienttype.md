# cmf.setRecipientType()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setrecipienttype( long recipient, string type )`

## Description
Sets the type of the recipient identified by *recipient* to the value *type.* The listed types are only examples and new types can be introduced at any time.

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `string` | `type` |  The type of the recipient: “FAX” | “TELEX” | “SMTP” | “SMS “ | “SITA” | “BAAN” | …  |

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
