# http.queryparamlist.add()

## Syntax:
`#include <bic_httpclt>`
`function void http.queryparamlist.add( long queryparamlist, const string name, const string value )`

## Description
Adds a name-value query parameter pair to an http.queryparamlist object.

## Arguments
| | | |
|---|---|---|
| `long` | `queryparamlist` |  an http.queryparamlist object  |
| `const string` | `name` |  the name of a query parameter  |
| `const string` | `value` |  the value of a query parameter  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.queryparamlist object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
