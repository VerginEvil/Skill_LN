# cmf.getDisplay()

## Syntax:
`function long cmf.getdisplay( long mid, ref enum display )`

## Description
Gets the display option of this message identified by *mid* and put it in the variable *display*.

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `ref enum` | `display` |  "TRUE": message shows before sending. User interface based service will be started. "FALSE": message is send without showing it first. UI-based and non ui-based service(s) can be started  |

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
