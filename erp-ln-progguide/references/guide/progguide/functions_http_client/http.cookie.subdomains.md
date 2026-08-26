# http.cookie.subdomains()

## Syntax:
`#include <bic_httpclt>`
`function boolean http.cookie.subdomains( long cookie )`

## Description
Returns whether an http.cookie object only applies to a single host or multiple hosts in the domain.
If the domain does not start with a dot (e.g. www.example.com), the subdomains flag is false. If the domain starts with a dot (e.g. .example.com), the subdomains flag is true.

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
true if the cookie applies to subdomains, else false

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)
- [HTTP Client synopsis](synopsis.md)
