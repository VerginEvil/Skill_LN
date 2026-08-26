# cmf.getNextAddress()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getnextaddress( long aid, long previous )`

## Description
Retrieves the next address child element in the address list root element identified by *aid*. If *previous* is 0 (zero) the id of the first entry on the addresslist is returned with type element. Else, the entry following the entry identified by previous is returned.

## Arguments
| | | |
|---|---|---|
| `long` | `aid` |  Identification of the address list.  |
| `long` | `previous` |  Index in the address list.  |

## Return values
| | |
|---|---|
| <> 0 | Id of address list child element. |
| 0 | End of child elements reached or invalid address list id supplied.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
