# cmf.addAddressEntry()

## Syntax:
`#include <bic_cmf>`
`function long cmf.addaddressentry( long aid, string role, string name, string address, string addresstype, [ domain ttcmf.catg key, domain ttcmf.catg category ] )`

## Description
Creates an address child node in the address list aid. The attributes of the node are provided by the parameters of the function.
Note: If an argument is left empty and the attribute is currently present in the message object, it will be removed completely.

## Arguments
| | | |
|---|---|---|
| `long` | `aid` |  Identification of the address list.  |
| `string` | `role` |    |
| `string` | `name` |  Recipient name  |
| `string` | `address` |  Recipient address  |
| `string` | `addresstype` |  Recipient type of address (fax, telex, smtp and so on.)  |
| `[ domain ttcmf.catg` | `key ]` |  The key and the category of the recipient (that make a primary key) to easily find the address entry of this recipient in the address book.  |
| `[ domain ttcmf.catg` | `category ]` |    |

## Return values
| | |
|---|---|
| <> 0 | Object id of addresslist entry. |
| 0 | Error creating entry (most likely invalid address list id). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
