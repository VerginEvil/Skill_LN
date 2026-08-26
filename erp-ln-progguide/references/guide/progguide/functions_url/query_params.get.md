# query_params.get()

## Syntax:
`#include <bic_web>`
`function boolean query_params.get( long query_params_instance, const string name, ref string value )`

## Description
Retrieves the first value of the specified query parameter from a query_params instance. Use [query_params.get_values()](query_params.get_values.md) to get all values as a string array.
The function returns `true` if the specified query parameter was found.

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `const string` | `name` |  A query parameter name.  |
| `ref string` | `value` |  The retrieved first value of the query parameter; if a based string is passed, it will be resized such that the complete value fits.  |

## Return values
| | |
|---|---|
| true | The specified query parameter was found. |
| false | The specified query parameter was not found; note that in this case the `value` parameter is not touched.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

string	sort_order(1) based

if not query_params.get(query_params, "sort-order", sort_order) then
	|* sort-order not found; set a default value
	str.assign(sort_order, "asc")
endif
```

## Availability
This function is available in the following TIV level ranges:
- 2153 - 2199 (ES 10.5.2.1)
- 2231 - 2299 (ES 10.6.1.1)
- 2393 - 2399 (ES 10.7.4.1)
- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
