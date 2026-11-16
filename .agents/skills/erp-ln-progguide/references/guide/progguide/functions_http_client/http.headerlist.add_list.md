# http.headerlist.add_list()

## Syntax:
`#include <bic_httpclt>`
`function void http.headerlist.add_list( long headerlist, long other_headerlist )`

## Description
Adds the contents of another http.headerlist to an http.headerlist object.
When an HTTP header already exists, it is overwritten. The only exception is the Set-Cookie header, which can occur multiple times in a headerlist.

## Arguments
| | | |
|---|---|---|
| `long` | `headerlist` |  an http.headerlist object  |
| `long` | `other_headerlist` |  another http.headerlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed ids must be valid http.headerlist objects

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
