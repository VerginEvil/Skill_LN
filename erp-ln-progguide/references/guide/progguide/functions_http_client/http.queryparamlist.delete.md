# http.queryparamlist.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.queryparamlist.delete( long queryparamlist )`

## Description
Deletes an http.queryparamlist object. Any contained name-value query parameter pairs are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `queryparamlist` |  an http.queryparamlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.queryparamlist object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
