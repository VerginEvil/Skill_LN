# cmf.getTaskTotalwork()

## Syntax:
`#include <bic_cmf>`
`function long cmf.gettasktotalwork( long tid, ref string totalwork )`

## Description
Gets the totalwork of the task identified by *tid* and return string into *totalwork.*

## Arguments
| | | |
|---|---|---|
| `long` | `tid` |  The Infor LN eMessage Connector task object identification.  |
| `ref string` | `totalwork` |  The total work for the task.  |

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
