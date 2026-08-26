# Json.addNumber()

## Syntax:
`#include <bic_json>`
`function [long] Json.addNumber( long json_array, long|double value )`

## Description
Convenience function for directly adding a 3GL long or double value to a JSON array. The 3GL long or double value is first converted to a JSON number value, which is then added to the array.
The function is a shorthand for: `Json.add(json, Json.newNumber(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long|double` | `value` |  The 3GL long or double value for which a JSON number value is created, which is then added to the array.  |

## Return values
Optional, the new JSON number value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
