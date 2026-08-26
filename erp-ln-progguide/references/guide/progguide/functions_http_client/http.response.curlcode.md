# http.response.curlcode()

## Syntax:
`#include <bic_httpclt>`
`function long http.response.curlcode( long response )`

## Description
Returns the cURL code stored in the response object. A cURL code of 0 means that communication was successful. Any other code indicates that communication was not successful. Reasons may be e.g. that the host could not be resolved, or (in case of https) that there are issues with the certificate(s).
Note that a cURL code of 0 only tells that communication was successful. This does however not tell whether the HTTP request succeeded. Use http.response.statuscode() to check whether the HTTP request could be handled by the webserver.
Use function http.response.error_message() to retrieve an English description of the cURL error.

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Return values
a cURL code, 0 means OK, any other code indicates an error

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
