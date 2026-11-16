# cmf.setDueDate()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setduedate( long mid, domain ttutc duedate )`

## Description
Sets the duedate of the message identified by *mid* to the value *duedate.* In case this message is routed through Microsoft Outlook, the message follow-up flag is set together with the indicated duedate.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `domain ttutc` | `duedate` |  Message duedate time.  |

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
