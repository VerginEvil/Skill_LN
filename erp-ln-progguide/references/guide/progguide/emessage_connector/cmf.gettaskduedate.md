# cmf.getTaskDuedate()

## Syntax:
`#include <bic_cmf>`
`function long cmf.gettaskduedate( long tid, ref domain ttutc duedate )`

## Description
Gets the task duedate of the task identified by *tid* and return it in the utc date *duedate.*

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `ref domain ttutc` | `duedate` |  The date by which the task must be finished.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object or element not present. |
| -2 | Date conversion error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
