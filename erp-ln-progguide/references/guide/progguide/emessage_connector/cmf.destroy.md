# cmf.destroy()

## Syntax:
`#include <bic_cmf>`
`function long cmf.destroy( long mid )`

## Description
Destroys the Infor LN eMessage Connector (message) object identified by id. This function can also be used to destroy recipient objects, attachment objects, etc.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
