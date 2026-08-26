# http.mimepartlist.add_list()

## Syntax:
`#include <bic_httpclt>`
`function void http.mimepartlist.add_list( long mimepartlist, long other_mimepartlist )`

## Description
Adds the contents of another http.mimepartlist to an http.mimepartlist object.

## Arguments
| | | |
|---|---|---|
| `long` | `mimepartlist` |  an http.mimepartlist object  |
| `long` | `other_mimepartlist` |  another http.mimepartlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2220.

## Preconditions
- the passed ids must be valid http.mimepartlist objects

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
