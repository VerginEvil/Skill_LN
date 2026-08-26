# Json.longAt()

## Syntax:
`#include <bic_json>`
`function long Json.longAt( long json_array, long idx )`

## Description
Convenience function for directly returning the 3GL long value of the JSON number value that is stored at the specified index in a JSON array.
Note that if the actual value stored in the JSON number is a double value, the value is truncated. E.g. 1.234 becomes 1.
The function is a shorthand for: `int(Json.numberAt(json, idx))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index in the array to get the value from.  |

## Return values
The JSON number value stored at the specified index, as a 3GL long value.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.
- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
