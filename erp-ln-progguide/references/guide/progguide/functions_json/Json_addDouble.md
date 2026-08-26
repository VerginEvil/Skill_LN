# Json.addDouble()

## Syntax:
`#include <bic_json>`
`function [long] Json.addDouble( long json_array, double value )`

## Description
Convenience function for directly adding a 3GL double value to a JSON array. The 3GL double value is first converted to a JSON number value, which is then added to the array.
The function is an alias for: `Json.addNumber(json, value)`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `double` | `value` |  The 3GL double value for which a JSON number value is created, which is then added to the array.  |

## Return values
Optional, the new JSON number value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2370.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
