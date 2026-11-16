# cmf.getService()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getService( string addresstype, enum user_interaction, enum resolve, ref string service )`

## Description
Returns the name of the service that supports the addresstype specified by the variables *addresstype*, *user_interaction* and *resolve*. The enum variables use the same enum types as their respective fields in the Infor LN eMessage Connector Address Types by Service table.

## Arguments
| | | |
|---|---|---|
| `string` | `addresstype` |  Specify the Infor LN eMessage Connector address type, for example, smtp, fax, telex and so on.  |
| `enum` | `user_interaction` |  Specify if the service must allow user interaction before completion of the message transfer. "YES"|"NO"  |
| `enum` | `resolve` |  Specify if the service should have resolve capability when given a name and address type. "YES"|"NO"  |
| `ref string` | `service` |  Returns the service identification that supports given parameters.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | No matching service found. The value of *service* is undefined in this case. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
