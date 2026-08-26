# http.response.bodystream()

## Syntax:
`#include <bic_httpclt>`
`function long http.response.bodystream( long response )`

## Description
Returns the stream id of the response body. It is not necessary to rewind the stream, the position is already at the start of the data retrieved from the server. In case a stream id was passed using the HTTP_RESPONSE_BODY option, this returns that stream id.

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Return values
a stream id

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
