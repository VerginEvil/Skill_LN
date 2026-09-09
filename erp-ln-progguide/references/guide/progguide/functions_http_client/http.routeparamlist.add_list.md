# http.routeparamlist.add_list()

## Syntax:
`#include <bic_httpclt>`
`function void http.routeparamlist.add_list( long routeparamlist, long other_routeparamlist )`

## Description
Adds the contents of another http.routeparamlist to an http.routeparamlist object. If route parameters already exist, they are replaced.

## Arguments
| | | |
|---|---|---|
| `long` | `routeparamlist` |  an http.routeparamlist object  |
| `long` | `other_routeparamlist` |  another http.routeparamlist object  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed ids must be a valid http.routeparamlist objects

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
