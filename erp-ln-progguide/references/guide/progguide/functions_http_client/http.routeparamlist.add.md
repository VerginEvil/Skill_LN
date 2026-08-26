# http.routeparamlist.add()

## Syntax:
`#include <bic_httpclt>`
`function void http.routeparamlist.add( long routeparamlist, const string name, const string value )`

## Description
Adds a name-value route parameter pair to an http.routeparamlist object.

## Arguments
| | | |
|---|---|---|
| `long` | `routeparamlist` |  an http.routeparamlist object  |
| `const string` | `name` |  the name of a route parameter  |
| `const string` | `value` |  the value of a route parameter  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.routeparamlist object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
