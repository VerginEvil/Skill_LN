# Json.at()

## Syntax:
`#include <bic_json>`
`function long Json.at( long json_array, long idx )`

## Description
Returns the JSON value that is stored at the specified index in a JSON array.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index in the array to get the value from.  |

## Return values
The JSON value that is stored in the JSON array at the specified index.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.
- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
