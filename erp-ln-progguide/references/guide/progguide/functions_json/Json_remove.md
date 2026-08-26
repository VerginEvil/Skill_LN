# Json.remove()

## Syntax:
`#include <bic_json>`
`function void Json.remove( long json_array, long idx )`

## Description
Removes the JSON value stored at the specified index in a JSON array. All values having a index higher than the specified index will be shifted one position to the left.
In case the JSON value that is removed is of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY all contained members are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index in the array of which the value must be removed.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2431.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.
- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
