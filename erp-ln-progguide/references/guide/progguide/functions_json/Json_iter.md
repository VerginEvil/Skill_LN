# Json.iter()

## Syntax:
`#include <bic_json>`
`function long Json.iter( long json_value )`

## Description
Returns an iterator which can be used to traverse the members of a JSON object or JSON array. On return the iterator points to the first member.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON object or array.  |

## Return values
An iterator pointing to the first member of a JSON object or JSON array, or 0 in case the JSON object or JSON array has no members.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
