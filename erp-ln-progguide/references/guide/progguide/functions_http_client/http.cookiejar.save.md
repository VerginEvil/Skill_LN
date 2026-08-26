# http.cookiejar.save()

## Syntax:
`#include <bic_httpclt>`
`function long http.cookiejar.save( long cookiejar, const string file )`

## Description
Saves the contents of an http.cookiejar object in a file. The contents of this file is overwritten.
The cookies are stored in Netscape format, in which each cookie is a string consisting of the following 7 parts, separated by tabs:
- domain
- subdomains (TRUE/FALSE)
- path
- secure (TRUE/FALSE)
- expires
- name
- value (can be empty)  See https://curl.se/docs/http-cookies.html for more info.

## Arguments
| | | |
|---|---|---|
| `long` | `cookiejar` |  an http.cookiejar object  |
| `const string` | `file` |  the path of the file to write to  |

## Return values
| | |
|---|---|
| 0 | success |
| <> 0 | an I/O error, like ENOSPC |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookiejar object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
