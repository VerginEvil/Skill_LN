# http.send()

## Syntax:
`#include <bic_httpclt>`
`function long http.send( const string method, const string url, ... )`

## Description
Sends an HTTP request to a URL.

## Arguments
| | | |
|---|---|---|
| `const string` | `method` |  an HTTP method, like "GET", "POST", "PUT", etc.  |
| `const string` | `url` |  the URL to send the request to  |
| `` | `...` |  Attributes to specify all kinds of options for the HTTP request, the following attributes are supported:  |

## Return values
an http.response object; check the response object for information about whether the request succeeded

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- passed number of arguments must be valid
- passed argument types must be valid
- passed attributes/flags must be known

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
