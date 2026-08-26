# http.headerlist.add()

## Syntax:
`#include <bic_httpclt>`
`function void http.headerlist.add( long headerlist, const string name, const string value )`

## Description
Adds a name-value HTTP header pair to an http.headerlist object.
Note that adding an HTTP header multiple times with the same name), overwrites the already existing one. The only exception is the Set-Cookie which can occur multiple times in the headerlist.
HTTP header names are searched in a case-insensitive way. So e.g. "Content-Type" is equal to "content-type".

## Arguments
| | | |
|---|---|---|
| `long` | `headerlist` |  an http.headerlist object  |
| `const string` | `name` |  an HTTP header name  |
| `const string` | `value` |  the value of the HTTP header  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- the passed id must be a valid http.headerlist object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
