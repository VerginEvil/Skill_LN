# client.upload.file

## Syntax:
`#include <bic_desktop>`
`function long client.upload.file( string destination, [ ref string client.filename, ref string mime.type ] )`

## Description
Upload a single file from the client and save this file on the server in the file location passed as the destination argument. Conversion of CRLF characters is only done for text files (file extension.txt or mime.type "text/plain"). All other file types are copied in binary mode. This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `string` | `destination` |  the file on the server to which the client file will be uploaded (user must have write permission).  |
| `[ ref string` | `client.filename ]` |  the original name of this file on the client  |
| `[ ref string` | `mime.type ]` |  optional string representing the MIME Media type of the file. The official list can be found here: [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).  |

## Return values
| | |
|---|---|
| 0 | success |
| < 0 | when an error occurred (for instance destination is a directory) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
