# client.get.media.type

## Syntax:
`#include <bic_desktop>`
`function string client.get.media.type( const string source )`

## Description
Returns the MIME media type based on the extension of the filename.

## Arguments
| | | |
|---|---|---|
| `const string` | `source` |  Specifies the file for which to determine the MIME Media type based on its file extension.  |

## Return values
string representing the MIME Media type of the file. The official list can be found here: https://www.iana.org/assignments/media-types/media-types.xhtml.

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Related topics
- [Client file access overview](overview.md)
- [Client file access synopsis](synopsis.md)
