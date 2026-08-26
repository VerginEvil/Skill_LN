# vwr.bms.received

## Syntax:
`#include <bic_vwr>`
`function void vwr.bms.received( long sender.id, const string mask(), const string mss(), long length )`

## Description
This is the callback function which must be defined in the 3GL script. This function will be called by the Document Viewer when a BMS message is received which is not internally known by the Document Viewer library. This can be used to receive PRCM messages. While in this callback function, the script can call functions like : prcm.bms.is.notification() and prcm.get.data().

## Arguments
| | | |
|---|---|---|
| `long` | `sender.id` |  The Baan process which has send this message.  |
| `const string` | `mask()` |  The mask with which the message has been send  |
| `const string` | `mss()` |  The actual BMS message  |
| `long` | `length` |  The length of the message mss  |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Document Viewer synopsis](synopsis.md)
- [Document Viewer overview](overview.md)
