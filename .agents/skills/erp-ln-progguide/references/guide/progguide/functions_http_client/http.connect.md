# http.connect()

## Syntax:
`#include <bic_httpclt>`
`function long http.connect( const string url,... )`

## Description
Sends a CONNECT HTTP request to a URL.

## Arguments
| | | |
|---|---|---|
| `const string` | `url` |  the URL to send the request to  |
|  | `...` | see [http.send()](http.send.md) for more information. |

## Return values
an http.response object; check the response object for information about whether the request succeeded
Note  Do not forget to delete the http.response object with [http.response.delete()](http.response.delete.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- passed number of arguments must be valid

- passed argument types must be valid

- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
