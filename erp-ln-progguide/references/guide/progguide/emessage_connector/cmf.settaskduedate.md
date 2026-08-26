# cmf.setTaskDuedate()

## Syntax:
`#include <bic_cmf>`
`function long cmf.settaskduedate( long tid, domain ttutc duedate )`

## Description
Sets the task duedate of the task identified by *tid* to the value *duedate.*

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `domain ttutc` | `duedate` |  The date by which the task must be finished.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Invalid cmf object. |
| -2 | Date conversion error. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
