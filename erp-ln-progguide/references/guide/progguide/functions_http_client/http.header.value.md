# http.header.value()

## Syntax:
`#include <bic_httpclt>`
`function string header.value( long header )`

## Description
Returns the HTTP header value of an http.header object.

## Arguments
| | | |
|---|---|---|
| `long` | `header` |  an http.header object  |

## Return values
the HTTP header value, e.g. "application/json" (which is a possible value of the "Content-Type" HTTP header)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.header object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
