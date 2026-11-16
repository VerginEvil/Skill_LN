# Json.insertString()

## Syntax:
`#include <bic_json>`
`function long Json.insertString( [long] json_array, long idx, string value )`

## Description
Convenience function for directly inserting a 3GL string value at the specified index in a JSON array. The 3GL string value is first converted to a JSON string value, which is then inserted into the array. All values at the specified index and above are shifted one position to the right.
Specifiying an index equal to the count + 1 effectively adds the value to the JSON array.
The function is a shorthand for: `Json.insert(json, idx, Json.newString(value))`

## Arguments
| | | |
|---|---|---|
| `[long]` | `json_array` |  A JSON array.  |
| `long` | `idx` |  The index to insert the JSON string value at.  |
| `string` | `value` |  The 3GL string value for which a JSON string value is created, which is then inserted into the array.  |

## Return values
Optional, the new JSON string value that has been inserted into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2431.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array + 1.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
