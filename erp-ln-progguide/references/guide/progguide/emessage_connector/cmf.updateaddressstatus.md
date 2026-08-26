# cmf.updateAddressStatus()

## Syntax:
`#include <bic_cmf>`
`function long cmf.updateaddressstatus( long entry_id, long errorcode )`

## Description
Updates the error status of an address entry. Entry_id is obtained from the function cmf.getNextAddress(). The possible values of errorcode are subdivided into two categories: errors which can also occur when the addresslist object is empty (global error variables used) and errors which only occur when the addresslist object is filled with one or more recipients: then the errorcode of the recipient is set to indicate the nature of the error. Possible values:

## Errors indicated by global variables
| | | |
|---|---|---|
| 0 | OK | No errors for this recipient |
| -1 | SERVICE_NOT_STARTED | Service could not be started: cmf.startService returned error  |
| -2 | SEND_ERROR | Cmf.send returned error |
| -3 | SERVICE_DISABLED | Service for current address type disabled in the Services (ttcmf030) table  |

## Errors indicated by errorcode
| | | |
|---|---|---|
| -10 | ADDRTYPE_NOT_SUPPORTED | Current addresstype not supported by any service.  |
| -11 | NO_SITA_SENDER_ADDRESS | From-recipient has no SITA-address in Address Book (ttcmf200), so all recipients with addresstype SITA could not be reached.  |
| -12 | MORE_SENDERS_FOUND | More than one from-recipient found. Message not send to all recipients  |
| -13 | NO_ADDRESS | No address found or set for this recipient. Message not sent to the intended recipient.  |
| -14 | LIST_MEMBER_NOT_ADDED | A member of a distribution list could not be added to the addresslist object.  |

## Arguments
| | | |
|---|---|---|
| `long` | `entry_id` |  The address list entry identification.  |
| `long` | `errorcode` |  See tables above.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | Error updating entry (most likely invalid address entry id).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
