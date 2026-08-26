# Json.addNull()

## Syntax:
`#include <bic_json>`
`function [long] Json.addNull( long json_array )`

## Description
Convenience function for adding a JSON null value to a JSON array.
The function is a shorthand for: `Json.add(json, Json.newNull())`

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |

## Return values
Optional, the new JSON null value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
