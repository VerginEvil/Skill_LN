# cmf.getAddressDetails()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getaddressdetails( long entry_id, ref string category, ref string key, ref string role, ref string name, ref string address, ref string addresstype, ref long errorcode )`

## Description
Retrieves the details of an address entry specified by entry_id. Entry_id is obtained from the function [cmf.getNextAddress()](cmf.getnextaddress.md) or [cmf.addAddressEntry()](cmf.addaddressentry.md). The attribute values for the object identified by entry_id are copied to the appropriate parameter variables.

## Arguments
| | | |
|---|---|---|
| `long` | `entry_id` |  The address list entry identification.  |
| `ref string` | `category` |  The recipient category.  |
| `ref string` | `key` |  The recipient key.  |
| `ref string` | `role` |  |
| `ref string` | `name` |  The recipient name.  |
| `ref string` | `address` |  The recipient address.  |
| `ref string` | `addresstype` |  The recipient addresstype.  |
| `ref long` | `errorcode` |  See cmf.updateAddressStatus()cmf.updateAddressStatus for the error codes.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error retrieving details (most probably invalid address entry id).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
