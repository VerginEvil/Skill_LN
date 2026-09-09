# query_params.value()

## Syntax:
`#include <bic_web>`
`function string query_params.value( long query_params_instance, const string name )`

## Description
Returns the first value of the specified query parameter from a query_params instance. Use [query_params.get_values()](query_params.get_values.md) to get all values as a string array.

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `const string` | `name` |  A query parameter name.  |

## Return values
The first value of the query parameter; if the parameter was not found, an empty string is returned.

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
