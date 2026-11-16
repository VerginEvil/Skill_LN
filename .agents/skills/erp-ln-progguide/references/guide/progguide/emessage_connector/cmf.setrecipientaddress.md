# cmf.setRecipientAddress()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setrecipientaddress( long recipient, string address )`

## Description
Sets the address of the recipient identified by *recipient* to the value *address.* An address could be a fax number, SMTP address, SMS number, and so on)

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `string` | `address` |  The address of the recipient.  |

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
