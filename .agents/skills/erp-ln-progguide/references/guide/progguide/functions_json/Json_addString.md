# Json.addString()

## Syntax:
`#include <bic_json>`
`function [long] Json.addString( long json_array, const string value )`

## Description
Convenience function for directly adding a 3GL string value to a JSON array. The 3GL string value is first converted to a JSON string value, which is then added to the array.
The function is a shorthand for: `Json.add(json, Json.newString(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `const string` | `value` |  The 3GL string value for which a JSON string value is created, which is then added to the array.  |

## Return values
Optional, the new JSON string value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
