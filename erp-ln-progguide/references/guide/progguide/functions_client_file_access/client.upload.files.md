# client.upload.files

## Syntax:
`#include <bic_desktop>`
`function long client.upload.files( string destination )`

## Description
Upload one or more files from the client and save these files in a server directory. Conversion of CRLF characters is only done for text files (file extension .txt or mime.type "text/plain"). All other file types are copied in binary mode. This function returns an id that can be used in the function [client.get.upload.file](client.get.upload.file.md) to obtain information of an uploaded file. This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `string` | `destination` |  the file on the server to which the client file will be uploaded (user must have write permission).  |

## Return values
| | |
|---|---|
| <> 0 | the id of the result object to be used by subsequent functions. This result object must be deleted using the function: [client.delete.upload.file.object](client.delete.upload.file.object.md) |
| 0 | when an error occurred (for instance destination is a directory) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
