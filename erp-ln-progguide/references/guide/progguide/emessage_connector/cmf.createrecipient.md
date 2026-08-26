# cmf.createRecipient()

## Syntax:
`#include <bic_cmf>`
`function long cmf.createrecipient( long mid, enum role )`

## Description
Creates a recipient entry of type *role* in the message identified by *mid* and returns the identification of the recipient object.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `enum` | `role` |  The recipient's role: “FROM” | “TO” | “CC” | “BCC” | “OBO” | “NOTIFY”  |

## Return values
| | |
|---|---|
| <> 0 | Recipient Id. |
| 0 | Invalid object id. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
