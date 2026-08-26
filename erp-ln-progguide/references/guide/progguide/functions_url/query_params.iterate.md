# query_params.iterate()

## Syntax:
`#include <bic_web>`
`function boolean query_params.iterate( long query_params_instance, ref long iterator, ref string name, ref string values(,), ref long num_values )`

## Description
Use this function to iterate all query parameters of a query_params instance.
Initialize the `iterator` argument to 0 to start the iteration. On return the `iterator` argument is updated. For each query parameter the name and the values are returned. The values of a query parameter are returned as strings in an array.
Typically this function is used in a `while ... endwhile` loop:
```

iterator = 0

while query_params.iterate(query_params, iterator, name, values, num_values)
        |* do something with the query parameter name and its values
endwhile
```

## Arguments
| | | |
|---|---|---|
| `long` | `query_params_instance` |  A query_params instance.  |
| `ref long` | `iterator` |  An iterator value. To get the first query parameter start with a value of 0; leave untouched to get the next query parameter.  |
| `ref string` | `name` |  The name of the retrieved query parameter. If a based string is passed, it will be resized so that the name will fit.  |
| `ref string` | `values(,)` |  The values of the retrieved query parameter as a string array. Note that it is not required to strip the values. Any trailing spaces in the original query parameter values are retained. If a based string array is passed, it will be resized such that all values will fit. If a non-based string array is specified, it may be that not all values are retrieved, and/or that values will be truncated.  |
| `ref long` | `num_values` |  The number of values that have been copied to the `values` string array.  |

## Return values
| | |
|---|---|
| true | The name and values of a query parameter have been returned. |
| false | No more query parameters to return. |

## Context
This function is implemented in the 4GL Tools and can be used in all script types.

## Example
```

long	query_params
long	iterator
string	name(1) based
long	num_values
string	values(1,1) based

query_params = query_params.parse("a=hi&b=bye&a=there+")
|* the query_params instance now contains 2 query parameters "a" and "b":
|* parameter "a" has 2 values, parameter "b" has 1 value

|* initialize the iterator
iterator = 0

while query_params.iterate(query_params, iterator, name, values, num_values)
	|* after the first call to query_params.iterate():
	|*   iterator has been updated to a non-zero value
	|*   name contains "a"
	|*   variable values has been resized to 2 elements with a size of 6 characters each
	|*   values(1,1) contains "hi" (without trailing spaces, so strip is not required)
	|*   values(1,2) contains "there " (the trailing space is retained, as it was part of the query string)
	|*   num_values is now 2

	|* after the second call to query_params.iterate():
	|*   iterator has been updated to another non-zero value
	|*   name contains "b"
	|*   variable values has been resized to 1 element with a size of 3 characters
	|*   values(1,1) contains "bye"
	|*   num_values is now 1

	|* after the third call to query_parameters.iterate(), the function return false
	|* which stops the while loop
endwhile

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
