# get.client.ip.address()

## Syntax:
`#include <bic_desktop>`
`function long get.client.ip.address( ref string ip.address )`

## Description
Get the IP address of the local client. In case of Baan Windows this is the client machine on which BW is running. In case of WebUI, this is the client machine on which the Internet Browser is running

## Arguments
| | | |
|---|---|---|
| `ref string` | `ip.address` |  Output argument which will contain the IP address of the client on return of this function.  |

## Return values
| | |
|---|---|
| true | Function succeeded, IP adress is filled. |
| false | Function failed, client IP address is unknown. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
