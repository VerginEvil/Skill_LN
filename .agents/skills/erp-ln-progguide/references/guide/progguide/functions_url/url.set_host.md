# url.set_host()

## Syntax:
`#include <bic_web>`
`function void url.set_host( long url_instance, const string host )`

## Description
Sets the host of a URL instance. This may be a hostname, or an IPv4/IPv6 address. Do not include the port number, use [url.set_port()](url.set_port.md) to set the port number.
This function ensures the specified host value is properly encoded before it is stored in the URL instance.

## Arguments
| | | |
|---|---|---|
| `long` | `url_instance` |  A URL instance.  |
| `const string` | `host` |  A host name, or an IPv4/IPv6 address.  |

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
