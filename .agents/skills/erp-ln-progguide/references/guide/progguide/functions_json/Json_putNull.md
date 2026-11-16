# Json.putNull()

## Syntax:
`#include <bic_json>`
`function long Json.putNull( [long] json_array, long idx )`

## Description
Convenience function for putting a JSON null value at the specified index in a JSON array.
The function is a shorthand for: `Json.put(json, idx, Json.newNull())`

## Arguments
| | | |
|---|---|---|
| `[long]` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index to put the JSON null value in.  |

## Return values
Optional, the new JSON null value that has been put into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
