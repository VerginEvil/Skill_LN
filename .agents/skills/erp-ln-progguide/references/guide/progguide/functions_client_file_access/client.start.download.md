# client.start.download

## Syntax:
`#include <bic_desktop>`
`function long client.start.download( long id )`

## Description
Start a download dialog showing a list of files constructed in advance with the functions [client.prepare.download](client.prepare.download.md) and [client.add.download.file](client.add.download.file.md) This function will return when the user closes the download dialog. This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  the download structure which was created using function: [client.prepare.download](client.prepare.download.md).  |

## Return values
| | |
|---|---|
| 0 | success |
| < 0 | when an error occurred (for instance invalid id) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
