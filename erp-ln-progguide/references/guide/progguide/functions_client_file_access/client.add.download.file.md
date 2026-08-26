# client.add.download.file

## Syntax:
`#include <bic_desktop>`
`function long client.add.download.file( long id, string source, [ string mime.type, string target ] )`

## Description
Add a file to the list of files to be downloaded to the client. The mime.type can be used to indicate the file type such that the browser has the option to start the client application which is associated with this mime.type. When the mime.type is not specified, the mime.type will be determined based on the file extension of the file specified in the optional target argument. When the optional target argument is also not specified, the mime.type will be determined based on the file extension of the file specified in the source argument Conversion of CRLF characters is only done for text files (file extension .txt or mime.type "text/plain"). All other file types are copied in binary mode. This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  the download structure which was created using function: [client.prepare.download](client.prepare.download.md).  |
| `string` | `source` |  Specifies the file on the server.  |
| `[ string` | `mime.type ]` |  optional string representing the MIME Media type of the file. The official list can be found here: https://www.iana.org/assignments/media-types/media-types.xhtml.  |
| `[ string` | `target ]` |  optional string representing the proposed file name on the client  |

## Return values
| | |
|---|---|
| 0 | success |
| < 0 | when an error occurred (for instance invalid source path) |
| -2 | The source file could not be opened. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
