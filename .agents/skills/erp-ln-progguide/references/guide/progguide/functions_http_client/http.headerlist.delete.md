# http.headerlist.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.headerlist.delete( long headerlist )`

## Description
Deletes an http.headerlist object. All contained http.header objects are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `headerlist` |  an http.headerlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.headerlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
