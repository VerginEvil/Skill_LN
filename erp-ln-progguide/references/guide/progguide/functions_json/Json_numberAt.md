# Json.numberAt()

## Syntax:
`#include <bic_json>`
`function double Json.numberAt( long json_array, long idx )`

## Description
Convenience function for directly returning the 3GL long or double value of the JSON number value that is stored at the specified index in a JSON array.
The function is a shorthand for: `Json.number(Json.at(json, idx))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index in the array to get the value from.  |

## Return values
The 3GL number value stored at the specified index, returned as a double.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
