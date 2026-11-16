# cmf.setTaskPriority()

## Syntax:
`#include <bic_cmf>`
`function long cmf.settaskpriority( long tid, enum priority )`

## Description
Sets the task priority of the task identified by *tid* to the value *priority.* This is a mandatory property for a Infor LN eMessage Connector task.

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `enum` | `priority` |  The task priority: "LOW" | "NORMAL" | "HIGH"  |

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
