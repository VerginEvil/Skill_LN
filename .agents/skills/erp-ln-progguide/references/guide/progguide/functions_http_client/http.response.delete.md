# http.response.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.response.delete( long response )`

## Description
Deletes an http.response object, including its related http.headerlist object. If the response object contains a body stream that was automatically opened, the stream will be closed as well.
Note  Do not forget to delete the http.response object as returned by the `http.get()`, `http.put()`, `http.post()`, etc. functions.
This helps preventing errors like `-11 (-EAGAIN)` related to opening files and streams.

## Arguments
| | | |
|---|---|---|
| `long` | `response` |  an http.response object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
