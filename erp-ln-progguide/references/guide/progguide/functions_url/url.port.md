# url.port()

## Syntax:
`#include <bic_web>`
`function long url.port( long url_instance )`

## Description
Returns the port number of a URL instance. This is -1 if the URL does not specify a port.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
| | |
|---|---|
| >= 0 | The port number of a URL instance. |
| -1 | The URL instance does not specify a port number. |

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
