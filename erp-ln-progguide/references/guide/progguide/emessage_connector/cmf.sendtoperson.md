# cmf.sendToPerson()

## Syntax:
`function long cmf.sendtoperson( long mid, long aid, long display, long show.progress, ref string message_string(), long convert, string filename1 ... )`

## Description
Takes the message object and sends it to the recipients in the addresslist object that is identified by aid.
Recipients are separated into groups by address type (fax, SMTP, telex, SITA, and so on). For each group a separate message object is built with the recipients in that group attached to it. The Infor LN eMessage Connector service for that address type is started and the message sent to it.
If no sender information is available, it will automatically be added. This holds also for the notify recipient (who, for example, gets the delivery reports). Also it's checked that the addresslist object contains only one sender (from-recipient).
Any errors encountered are stored for each recipient in the addresslist object. Infor LN eMessage Connector services opened by this function are not stopped. This is for efficiency purposes. It is expensive to start and stop services. This allows applications to make multiple calls to cmf.sendToPerson without incurring the overhead of service startup and shutdown. Instead another function will be provided to stop all services opened by this function (cmf.stopAllServices).

## Arguments
| | | |
|---|---|---|
| `long` | `mid` |  Message object identification.  |
| `long` | `aid` |  Identification of the address list.  |
| `long` | `display` |  |
| `long` | `show.progress` |  |
| `ref string` | `message_string()` |  Constructed error message which contains the number of recipients that could not be reached, and the error details. If no errors, message_string contains a success message  |
| `long` | `convert` |  |
| `string` | `filename1 ...` |   |

## Return values
| | |
|---|---|
| 0 | Success for all recipients. |
| -1 | Failure for some or all recipients (Check recipient list object).  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note
- Object id's can be negative
- The calling application is responsible for deleting message and address list object after this function has finished.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
