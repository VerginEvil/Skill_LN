# http.cookiejar.delete()

## Syntax:
`#include <bic_httpclt>`
`function void http.cookiejar.delete( long cookiejar )`

## Description
Deletes an http.cookiejar object. All contained http.cookie objects are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `cookiejar` |  an http.cookiejar object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookiejar object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
