# http.cookie.secure()

## Syntax:
`#include <bic_httpclt>`
`function boolean http.cookie.secure( long cookie )`

## Description
Returns whether an http.cookie object only applies to secure connections (like https).

## Arguments
| | | |
|---|---|---|
| `long` | `cookie` |  an http.cookie object  |

## Return values
true if the cookie applies to secure connections only, else false

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2400.

## Preconditions
- the passed id must be a valid http.cookie object

## Related topics
- [HTTP Client overview](overview.md)

- [HTTP Client synopsis](synopsis.md)
