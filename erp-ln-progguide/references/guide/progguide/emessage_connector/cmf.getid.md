# cmf.getId()

## Syntax:
`#include <bic_cmf>`
`function long cmf.getid( string messageld, string service, domain ttcmf.mdir message.direction, ref string error_string() )`

## Description
Creates a path to the header.xml file, which consists of the message storage path in the Services (ttcmf030) table and inbox or outbox (depending on message direction) and header.xml. This file is opened in read mode and then parsed with function xml.read which returns the bshell-wide unique object ID of the message object, which is often needed to call other functions in this library.

## Arguments
| | | |
|---|---|---|
| `string` | `messageld` |  Unique identification of a message within Infor LN eMessage Connector.  |
| `string` | `service` |  Service offered by a provider, for example, Fax or Email.  |
| `domain ttcmf.mdir` | `message.direction` |  This is an enumerated field that indicates whether the message was inbound (to the Bshell) or outbound (from the Bshell). This field also indicates whether the message is stored in the inbox or outbox subdirectories of the message storage directory. The possible values are: "ttcmf.mdir.inbound|ttcmf.mdir.outbound".  |
| `ref string` | `error_string()` |  Detailed error information.  |

## Return values
| | |
|---|---|
| <> 0 | mid = Bshell-wide unique message ID. |
| 0 | mid = no valid object id error_string contains detailed error information.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)
- [eMessage Connector synopsis](synopsis.md)
- [eMessage Connector examples](examples.md)
