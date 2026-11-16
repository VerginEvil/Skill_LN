# cmf.messageDialog()

## Syntax:
`#include <bic_cmf>`
`function long cmf.messagedialog( long mode, long show, [ long show.message ] )`

## Description
Launches a Message dialog box.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |    |
| `long` | `show` |    |
| `[ long` | `show.message ]` |  If the optional show.message argument is set to 1, cmf.sendToPerson will start up a user interface based service (if available) for each message type found in the addresslist object.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error launching the Message Dialog. |
| -2 | Error: invalid argument value(s). |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
