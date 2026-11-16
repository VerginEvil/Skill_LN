# url.path()

## Syntax:
`#include <bic_web>`
`function string url.path( long url_instance )`

## Description
Returns the path of a URL instance. This is an empty string if the URL does not specify an path.
Note  The path is returned in its non-decoded form. The reason is that the returned path will typically need further processing, like traversing the individual path segments by searching for the path separator (forward slash). If the path string would be returned in its decoded form, it would be impossible to distinguish between real path separators and forward slashes as part of path segments.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
The non-decoded path of a URL instance.

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
