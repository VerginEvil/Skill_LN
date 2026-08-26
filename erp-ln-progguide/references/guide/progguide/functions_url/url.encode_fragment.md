# url.encode_fragment()

## Syntax:
`#include <bic_web>`
`function string url.encode_fragment( const string fragment )`

## Description
Encodes a fragment according to RFC 3986, so it can be safely used in a URL.
The following characters are not escaped:
- The 'pchar' set of characters. This set consists of:
-
- The 'unreserved' set of characters: `a-zA-Z0-9-._~`
- The 'sub-delims' set of characters: `!$&'()*+,;=`
- The characters: `:@`
- The path separator and the question mark: `/?`

## Arguments
| | | |
|---|---|---|
| `const string` | `fragment` |  A URL fragment.  |

## Return values
The URL encoded fragment.

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
