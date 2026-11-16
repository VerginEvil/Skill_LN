# Json.add()

## Syntax:
`#include <bic_json>`
`function [long] Json.add( long json_array, long json_value )`

## Description
Adds a JSON value at the end of a JSON array.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `json_value` |  The new JSON value to set.  |

## Return values
Optional, the new JSON value that has been added to the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'json_value' is a JSON value.

- Parameter 'json_value' is detached (i.e. not assigned to a member of another JSON object or array).

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
