# Json.putDouble()

## Syntax:
`#include <bic_json>`
`function long Json.putDouble( [long] json_array, long idx, double value )`

## Description
Convenience function for directly putting a 3GL double value at the specified index in a JSON array. The 3GL double value is first converted to a JSON number value, which is then put into the array.
The function is an alias for: `Json.putNumber(json, idx, value)`

## Arguments
| | | |
|---|---|---|
| `[long]` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index to put the JSON number value in.  |
| `double` | `value` |  The 3GL double value for which a JSON number value is created, which is then put into the array.  |

## Return values
Optional, the new JSON number value that has been put into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.
- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
