# get.client.directory()

## Syntax:
`#include <bic_desktop>`
`function string get.client.directory( const string id )`

## Description
*Deprecated.* This function returns the folder, on the local client, related to a given id. In case of Baan Windows this is the folder that is defined by the ${id} environment variable on the local client. In case of WebUI, this is a folder, on the client machine on which the Internet Browser is running, related to the id.

## Arguments
| | | |
|---|---|---|
| `const string` | `id` |  Input argument which will contain the id for which to determine the related client folder. In WebUI only the "BSE_TMP" id is supported.  |

## Return values
The folder related to the given id. In case of Baan Windows, the return value contains the value of the ${BSE_TMP} client environment variable. In case of WebUI, the return value contains the name of the default temporary folder on the client machine. The return value is empty when an id is used for which no folder was defined.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Notes  This function is not supported in LN UI. See the [Implementing LN UI support](../webtop/htmlui_adoption.md) for more information.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
