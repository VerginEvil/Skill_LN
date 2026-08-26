# http.routeparamlist.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.routeparamlist.delete( long routeparamlist )`

## Description
Deletes an http.routeparamlist object. Any contained name-value route parameters pairs are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `routeparamlist` |  an http.routeparamlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.routeparamlist object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
