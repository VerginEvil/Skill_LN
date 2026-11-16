# query_params.has()

## Syntax:
`#include <bic_web>`
`function boolean query_params.has( long query_params_instance, const string name )`

## Description
Tells whether a query_params instance contains the specified query parameter.

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `const string` | `name` |  A query parameter name.  |

## Return values
| | |
|---|---|
| true | The specified query parameter was found. |
| false | The specified query parameter was not found |

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
