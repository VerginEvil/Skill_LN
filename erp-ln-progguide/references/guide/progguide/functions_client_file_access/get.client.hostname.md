# get.client.hostname()

## Syntax:
`#include <bic_desktop>`
`function long get.client.hostname( ref string hostname )`

## Description
This returns the hostname of the local client (if available). In case of Baan Windows this is the client machine on which BW is running. In case of WebUI, this is the client machine on which the Internet Browser is running.

## Arguments
| | | |
|---|---|---|
| `ref string` | `hostname` |  Output argument which will contain the fully qualified hostname of the client on return of this function.  |

## Return values
| | |
|---|---|
| true | Function succeeded, hostname is filled. |
| false | Function failed, client hostname is unknown. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
