# cmf.setRecipientReasonstring()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setrecipientreasonstring( long recipient, string reasonstring(100) )`

## Description
Sets the (human-readable) reason string of the recipient identified by *recipient* to the value *reasonstring.* The reason string is used only in case of a non-delivery of a message to a recipient.

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `string` | `reasonstring(100)` |  The description of the reason why the message could not be delivered.  |

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
