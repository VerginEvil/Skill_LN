# cmf.getRecipientReasonstring()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getrecipientreasonstring( long recipient, ref string reasonstring )`

## Description
Gets the reason string of the recipient identified by *recipient* and returns it in the string *reasonstring.*

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `ref string` | `reasonstring` |  The description of the reason why the message could not be delivered.  |

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
