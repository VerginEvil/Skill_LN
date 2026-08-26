# cmf.setClass()

## Syntax:
`function long cmf.setclass( long mid, string class )`

## Description
Sets the message class of the message identified by *mid* to the value *class.*

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `string` | `class` |  Mandatory attribute for a message, identifying the meaning of a message: for example CMF.TASK for tasks, CMF.APPOINTMENT for appointments and so on.  |

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
