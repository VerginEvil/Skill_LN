# url.fragment()

## Syntax:
`#include <bic_web>`
`function string url.fragment( long url_instance )`

## Description
Returns the decoded fragment of a URL instance. This is an empty string if the URL does not specify an fragment.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |

## Return values
The decoded fragment of a URL instance.

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
