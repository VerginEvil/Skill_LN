# http.response.request_url()

## Syntax:
`#include <bic_httpclt>`
`function string http.response.request_url( long response )`

## Description
Returns the URL of the request for which the response was created. The HTTP method and the URL are stored to identify to what request the response object belongs.

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Return values
the request URL

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
