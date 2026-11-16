# cmf.getRecipientName()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getrecipientname( long recipient, ref string name )`

## Description
Gets the name of the recipient identified by *recipient* and returns it in the string *name.*

## Arguments
| | | |
|---|---|---|
| `long` | `recipient` |  The recipient identification.  |
| `ref string` | `name` |  The name of the recipient.  |

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
