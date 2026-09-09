# Json.put()

## Syntax:
`#include <bic_json>`
`function [long] Json.put( long json_array, long idx, long json_value )`

## Description
Puts a JSON value at the specified index in a JSON array. The existing JSON value is deleted and replaced with the new JSON value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  *idx* is the index to put the JSON value in.  |
| `long` | `json_value` |  The new JSON value to set.  |

## Return values
Optional, the new JSON value that has been put into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.

- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array.

- Parameter 'json_value' is a JSON value.

- Parameter 'json_value' is detached (i.e. not assigned to a member of another JSON object or array).

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
