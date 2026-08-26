# http.cookiejar.load()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookiejar.load( ref long cookiejar, const string file )`

## Description
Fills an http.cookiejar object with the cookies stored in the specified file.
If no http.cookiejar object is specified, one is created. If an existing http.cookiejar object is specified it is cleared before loading from the specified file.
The file is expected to have the cookies stored in Netscape format, in which each cookie is a line consisting of the following 7 parts, separated by tabs:
- domain
- subdomains (TRUE/FALSE)
- path
- secure (TRUE/FALSE)
- expires
- name
- value (can be empty)  See https://curl.se/docs/http-cookies.html for more info.
Notes
- A line starting with # is treated as comments, except when the line starts with #HttpOnly_ which is a valid prefix for the cookie domain.
- Only basic checking is done; whether the parts match with each other is not checked!

## Arguments
| | | |
|---|---|---|
| `ref long` | `cookiejar` |  an http.cookiejar object; if 0, a new http.cookiejar object is created; upon return of the function the id of the new http.cookiejar object is returned in this parameter  |
| `const string` | `file` |  the path to the cookie file  |

## Return values
| | |
|---|---|
| 0 | success |
| <> 0 | an I/O error, like ENOENT |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be 0 or a valid http.cookiejar object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
