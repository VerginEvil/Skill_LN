# cmf.setDisplay()

## Syntax:
`#include <bic_cmf>`
`function long cmf.setdisplay( long mid, enum display )`

## Description
Sets the display option of this message identified by *mid* to the value *display*.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `enum` | `display` |  When set to "TRUE" the message will be shown before sending it. A User interface based service will be started. "FALSE" means the message will be sent without showing it first. UI-based and non ui-based service(s) can be started  |

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
