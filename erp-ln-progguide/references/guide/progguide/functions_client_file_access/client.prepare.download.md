# client.prepare.download

## Syntax:
`#include <bic_desktop>`
`function long client.prepare.download( )`

## Description
Prepare the download of one or more server files. This function is only supported for LN UI.

## Return values
| | |
|---|---|
| <> 0 | the id of the download structure which can be used by subsequent calls. This id can be passed to [client.add.download.file](client.add.download.file.md) function to add a file to the download or to the [client.start.download](client.start.download.md) function to start the download.  |
| 0 | when an error occurred (for instance when using this function in WebUI or LN UI) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
