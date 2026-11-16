# cmf.getAddressBookKey()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getaddressbookkey( long entry.id, ref string key, ref string category )`

## Description
Gets the two key fields of the Address Book (ttcmf200) of the recipient identified by entry.id and returns them in the strings key and category.

## Arguments
| | | |
|---|---|---|
| `long` | `entry.id` |  The address list entry identification.  |
| `ref string` | `key` |  The recipient key.  |
| `ref string` | `category` |  The recipient category.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error retrieving category and key: probably invalid recipient id. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

- With these two values it's very easy to retrieve data from the Address Book about a recipient

- Category and key are set using cmf.addAddressEntrycmf.addAddressEntry

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
