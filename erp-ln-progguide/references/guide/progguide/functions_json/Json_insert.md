# Json.insert()

## Syntax:
`#include <bic_json>`
`function [long] Json.insert( long json_array, long idx, long json_value )`

## Description
Inserts a JSON value at the specified index in a JSON array. All values at the specified index and above are shifted one position to the right.
Specifiying an index equal to the count + 1 effectively adds the value to the JSON array.

## Arguments
| | | |
|---|---|---|
| `long` | `json_array` |  A JSON array.  |
| `long` | `idx` |  *idx* is the index to put the JSON value in.  |
| `long` | `json_value` |  The JSON value to insert.  |

## Return values
Optional, the JSON value that has been inserted into the JSON array.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2431.

## Preconditions
- Parameter 'json_array' is a JSON value of type JSON_TYPE_ARRAY.
- Parameter 'idx' is greater than 0 and less than or equal to the number of values in the array + 1.
- Parameter 'json_value' is a JSON value.
- Parameter 'json_value' is detached (i.e. not assigned to a member of another JSON object or array).

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
