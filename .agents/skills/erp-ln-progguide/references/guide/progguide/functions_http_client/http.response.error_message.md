# http.response.error_message()

## Syntax:
`#include <bic_httpclt>`
`function string http.response.error_message( long response )`

## Description
Call this to retrieve an error message in case there was an error while sending the request.
In case the cURL code is zero (0), this returns "No error"

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Return values
an English error message, which can be used for debugging and/or logging

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
