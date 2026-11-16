# url.set_path()

## Syntax:
`#include <bic_web>`
`function void url.set_path( long url_instance, const string path )`

## Description
Sets the path of a URL instance.
This function ensures the specified path value is properly encoded before it is stored in the URL instance.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |
| `const string` | `path` |  A path string, like `"/path/to/some/resource"`.  |

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
