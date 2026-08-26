# client.get.upload.file

## Syntax:
`#include <bic_desktop>`
`function string client.get.upload.file( long id, long index, [ ref string client.filename, ref string mime.type ] )`

## Description
Get the details about a file which is uploaded with function [client.upload.files](client.upload.files.md). This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  the id of the result object returned by [client.upload.files](client.upload.files.md).  |
| `long` | `index` |  one-based index of the uploaded file for which the information is requested.  |
| `[ ref string` | `client.filename ]` |  the original name of this file on the client.  |
| `[ ref string` | `mime.type ]` |  optional string representing the MIME Media type of the file. The official list can be found here: https://www.iana.org/assignments/media-types/media-types.xhtml.  |

## Return values
The server path name of the uploaded file or empty when an error occurred

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
