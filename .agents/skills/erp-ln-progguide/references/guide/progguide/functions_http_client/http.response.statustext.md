# http.response.statustext()

## Syntax:
`#include <bic_httpclt>`
`function string http.response.statustext( long response )`

## Description
Returns the HTTP response status text, like "OK" (for 200), "Not Found" (for 404), "Internal Server Error" (for 500), etc.

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Return values
an HTTP status text

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
