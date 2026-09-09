# Json.count()

## Syntax:
`#include <bic_json>`
`function long Json.count( long json_array )`

## Description
Returns the number of JSON values stored in a JSON array.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |

## Return values
The number of JSON values in the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
