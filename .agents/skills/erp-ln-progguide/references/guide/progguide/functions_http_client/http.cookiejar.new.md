# http.cookiejar.new()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookiejar.new( )`

## Description
Creates a new empty http.cookiejar object.
This can be used to keep track of cookies when doing multiple requests. When passed to a [http.get()](http.get.md), [http.post()](http.post.md) etc. call as the value of the HTTP_COOKIEJAR attribute, any applicable cookies from the cookiejar are sent to the server, and when the response is received, the cookiejar is updated with any received cookies from the server.

## Return values
a new http.cookiejar object

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
