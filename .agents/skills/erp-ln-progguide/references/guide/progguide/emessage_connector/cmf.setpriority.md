# cmf.setPriority()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setpriority( long mid, enum priority )`

## Description
Sets the priority of the message identified by *mid* to the value *priority.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `enum` | `priority` |  Message priority. “LOW” | “NORMAL” | “HIGH”.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
