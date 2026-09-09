# query_params.get_values()

## Syntax:
`#include <bic_web>`
`function long query_params.get_values( long query_params_instance, const string name, ref string values(,) )`

## Description
Retrieves all values of the specified query parameter from a query_params instance. The values are returned as a string array.
The function returns the number of values found.

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `const string` | `name` |  A query parameter name.  |
| `ref string` | `values(,)` |  The retrieved values of the query parameter. Note that it is not required to strip the values. Any trailing spaces in the original query parameter values are retained. If a based string array is passed, it will be resized such that all values will fit. If a non-based string array is specified, it may be that not all values are retrieved, and/or that values will be truncated.  |

## Return values
| | |
|---|---|
| > 0 | The number of values that have been copied to the `values` string array. |
| 0 | The specified query parameter was not found; note that in this case the `values` parameter is not touched. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

long	query_params
long	num_values
string	values(1,1) based

query_params = query_params.parse("a=hi&a=there+&b=bye&c=")
num_values = query_params.get_values(query_params, "a", values)

|* num_values is now 2
|* variable values has been resized to 2 elements with a size of 6 characters each
|* values(1,1) contains "hi" (without trailing spaces, so strip is not required)
|* values(1,2) contains "there " (the trailing space is retained, as it was part of the query string)

num_values = query_params.get_values(query_params, "b", values)

|* num_values is now 1
|* variable values has been resized to 1 element with a size of 3 characters
|* values(1,1) contains "bye"

num_values = query_params.get_values(query_params, "c", values)

|* num_values is now 1
|* variable values has been resized to 1 element with a size of 1 character
|* values(1,1) contains "" (no space, so strip is not required)

|* cleanup
query_params.delete(query_params)
free.mem(values)
```

## Availability
This function is available in the following TIV level ranges:

- 2153 - 2199 (ES 10.5.2.1)

- 2231 - 2299 (ES 10.6.1.1)

- 2393 - 2399 (ES 10.7.4.1)

- 2451 and above (ES 10.8.5)

## Related topics
- [URL Functions Overview](overview.md)
