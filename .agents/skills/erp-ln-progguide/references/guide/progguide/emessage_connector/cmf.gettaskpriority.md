# cmf.getTaskPriority()

## Syntax:
`function long cmf.gettaskpriority( long tid, ref enum priority )`

## Description
Gets the task priority of the task identified by *tid* and returns string into *priority.*

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `ref enum` | `priority` |  The task priority: "LOW" | "NORMAL" | "HIGH"  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error (most likely invalid object id or element not present). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
