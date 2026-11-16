# http.header.name()

## Syntax:
`#include <bic_httpclt>`
`function string http.header.name( long header )`

## Description
Returns the HTTP header name of an http.header object.

## Arguments
| | | |
|---|---|---|
| `long` | `header` |  an http.header object  |

## Return values
the HTTP header name, eg. "Content-Type"

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.header object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
