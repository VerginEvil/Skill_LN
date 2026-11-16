# client.show.url

## Syntax:
`#include <bic_desktop>`
`function long client.show.url( string url )`

## Description
This function opens a *URL* in an external browser window. The behavior is the same as function [open.url.local()](open.url.local.md) with the *mode* parameter set to *OPEN_URL_EXTERNAL*. This function is only supported in the WebUI and LN UI.

## Arguments
| | | |
|---|---|---|
| `string` | `url` |  This specifies the URL that needs to be started.  |

## Return values
| | |
|---|---|
| 0 | success |
| < 0 | when an error occurred (for instance invalid source path) |

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.
Notes  Due to browser security restrictions it is not possible to open a local (client side) file. So a url which starts with *file://{filepath}* will not open the local file.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)

- [Document Viewer overview](../functions_vwr/overview.md)
