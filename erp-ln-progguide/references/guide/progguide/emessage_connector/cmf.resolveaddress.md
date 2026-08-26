# cmf.resolveAddress()

## Syntax:
`#include <bic_cmf>`
`function long cmf.resolveaddress( ref domain ttcmf.catg category, ref domain ttcmf.catg key, ref domain ttcmf.defa addresstype, ref string address(), ref string message.str, [ string name(100) mb, long use.default ] )`

## Description
Selects address data of recipient identified by key and category from Address Book and sets address depending on value of addresstype. Address data is selected from Tools Address Book (table ttcmf200) if current company is 0 and from Infor Enterprise Server Address Book (table tccom130/131) if current company is not 0.
- If *key* and *category* arguments are empty, it is possible to search the Tools Address Book using the optional argument *name*. If more than one record is found, an error is returned. The Infor Enterprise Server Address Book cannot be searched using just a name. In this case a RECIPIENT_NOT_FOUND (-2) error is returned.
- If the argument *use.default* is set to true and *addresstype* is empty, the address is resolved using the default address type specified in the Address Book. If the *addresstype* argument is empty and *use.default* is not set to true, the address is not resolved.
- If the *key* and *category* arguments are both filled and also a *name* argument is supplied, then it is checked if they match. If they do not match, the *category* and *key* arguments are made empty and the Tools Address Book is searched for an entry with *name* = <name>. If exactly one entry is found the *category*, *key* and *address* argument are filled with the found values. Note: the Infor Enterprise Server Address Book cannot be searched with just a *name* argument. So in this case a RECIPIENT_NOT_FOUND (-2) error is returned.
- If *category* is ‘Distribution List’, the function stops immediately after the above check and returns SUCCESS (0). If the *category* and *key* arguments are empty and the *name* argument filled, the Tools Address Book (ttcmf200) is searched to determine if this name represents a distribution list, if so, the *key* argument is filled with the name of the list (ttcmf210.list) and the *category* argument is set to ‘Distribution List’.

## Arguments
| | | |
|---|---|---|
| `ref domain ttcmf.catg` | `category` |  Recipient's category.  |
| `ref domain ttcmf.catg` | `key` |  Recipient's key.  |
| `ref domain ttcmf.defa` | `addresstype` |  Recipient type of address (fax, telex, smtp and so on.)  |
| `ref string` | `address()` |  Recipient's actual address depending on the address type.  |
| `ref string` | `message.str` |   |
| `[ string` | `name(100) mb ]` |  The name of the recipient.  |
| `[ long` | `use.default ]` |  If true, the default address type for the recipient is used.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error: no address specified for addresstype in Address Book  |
| -2 | Error: recipient not found in Address Book |
| -3 | Error: more than one record found in Address Book  |
| -4 | Error: dll tcintdlltccom not found on server |
| -5 | Error: function tcint.dlltccom.start.addresses not found in dll tcintdlltccom.  |
| -6 | Error: key field must be filled if category is Business Contact  |
| -7 | Error: table tccom130 and/or tccom131 not found  |
| -8 | Error: something went wrong in execution of function tcint.dlltccom.start.addresses in DLL tcintdlltccom  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
