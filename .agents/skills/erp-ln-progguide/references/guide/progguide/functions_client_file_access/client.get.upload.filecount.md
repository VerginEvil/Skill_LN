# client.get.upload.filecount

## Syntax:
`#include <bic_desktop>`
`function long client.get.upload.filecount( long id )`

## Description
Get the number of files which are uploaded with function [client.upload.files](client.upload.files.md). This function is only supported for LN UI.

## Arguments
| | | |
|---|---|---|
| `long` | `id` |  the id of the result object returned by [client.upload.files](client.upload.files.md).  |

## Return values
| | |
|---|---|
| > 0 | the number of files uploaded |
| < 0 | when id is not a valid object returned by [client.upload.files](client.upload.files.md) |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)

- [Client file access synopsis](synopsis.md)
