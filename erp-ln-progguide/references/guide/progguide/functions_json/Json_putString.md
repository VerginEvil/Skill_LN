# Json.putString()

## Syntax:
`#include <bic_json>`
`function long Json.putString( [long] json_array, long idx, string value )`

## Description
Convenience function for directly putting a 3GL string value at the specified index in a JSON array. The 3GL string value is first converted to a JSON string value, which is then put into the array.
The function is a shorthand for: `Json.put(json, idx, Json.newString(value))`

## Arguments
| | | |
|---|---|---|
| `[long]` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index to put the JSON string value in.  |
| `string` | `value` |  The 3GL string value for which a JSON string value is created, which is then put into the array.  |

## Return values
Optional, the new JSON string value that has been put into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
