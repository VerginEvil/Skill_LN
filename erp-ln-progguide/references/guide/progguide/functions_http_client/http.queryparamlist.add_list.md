# http.queryparamlist.add_list()

## Syntax:
`#include <bic_httpclt>`
`function void http.queryparamlist.add_list( long queryparamlist, long other_queryparamlist )`

## Description
Adds the contents of another http.queryparamlist to an http.queryparamlist object.

## Arguments
| | | |
|---|---|---|
| `long` | `queryparamlist` |  an http.queryparamlist object  |
| `long` | `other_queryparamlist` |  another http.queryparamlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed ids must be a valid http.queryparamlist objects

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
