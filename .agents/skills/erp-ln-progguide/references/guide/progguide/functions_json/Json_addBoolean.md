# Json.addBoolean()

## Syntax:
`#include <bic_json>`
`function [long] Json.addBoolean( long json_array, boolean value )`

## Description
Convenience function for directly adding a 3GL boolean value to a JSON array. The 3GL boolean value is first converted to a JSON boolean value, which is then added to the array.
The function is a shorthand for: `Json.add(json, Json.newBoolean(value))`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `boolean` | `value` |  The 3GL boolean value for which a JSON boolean value is created, which is then added to the array.  |

## Return values
Optional, the new JSON boolean value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
