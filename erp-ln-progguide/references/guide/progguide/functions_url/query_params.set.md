# query_params.set()

## Syntax:
`#include <bic_web>`
`function void query_params.set( long query_params_instance, const string name, const string value )`

## Description
Sets a query parameter in a query_params instance. If the parameter already exists, any values are replaced by the specified one.
Note  Specify the query parameter name and value in their raw, unencoded form. Any required encoding is done by function [query_params.to_string()](query_params.to_string.md).

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `const string` | `name` |  A query parameter name.  |
| `const string` | `value` |  A query parameter value.  |

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
