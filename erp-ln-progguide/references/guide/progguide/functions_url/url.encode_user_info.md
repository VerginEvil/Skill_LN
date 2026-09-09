# url.encode_user_info()

## Syntax:
`#include <bic_web>`
`function string url.encode_user_info( const string user_info )`

## Description
Encodes a user info string according to [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986), so it can be safely used in a URL. A user info string has the format `user[:pwd]` (the `:pwd` part is optional).
The following characters are not escaped:

- The 'unreserved' set of characters: `a-zA-Z0-9-._~`

- The 'sub-delims' set of characters: `!$&'()*+,;=`

- A character that is specific to user info: `:`

## Arguments
| | | |
|---|---|---|
| `const string` | `user_info` |  A user and (optional) password combination, in the format `user[:pwd]`.  |

## Return values
The URL encoded user info string.

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
