# cmf.getCreateTime()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getcreatetime( long mid, ref domain ttutc createtime )`

## Description
Gets the message creation time of the message identified by *mid* and returns it into utc date *createtime.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref domain ttutc` | `createtime` |  UTC date the message was created.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id or element not present). |
| -2 | Date conversion error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
