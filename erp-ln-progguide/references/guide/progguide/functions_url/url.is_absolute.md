# url.is_absolute()

## Syntax:
`#include <bic_web>`
`function boolean url.is_absolute( long url_instance )`

## Description
Returns true if a URL instance represents an absolute URL. An absolute URL specifies a scheme, like `http`, `ftp`, etc.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
| | |
|---|---|
| true | The URL is an absolute URL. |
| false | The URL is not an absolute URL |

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
