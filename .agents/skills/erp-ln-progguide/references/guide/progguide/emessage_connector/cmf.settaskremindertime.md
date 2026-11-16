# cmf.setTaskReminderTime()

## Syntax:
`#include <bic_cmf>`
`function long cmf.settaskremindertime( long tid, domain ttutc remindertime )`

## Description
Sets the task remindertime of the task identified by *tid* to the value *remindertime.*

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `domain ttutc` | `remindertime` |  The task reminder time.  |

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
