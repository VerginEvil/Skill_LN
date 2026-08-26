# Json.iterNext()

## Syntax:
`#include <bic_json>`
`function long Json.iterNext( long json_value, long iter )`

## Description
Moves the iterator to the next member of a JSON object or JSON array.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON object or array.  |
| `long` | `iter` |  A JSON iterator.  |

## Return values
An iterator pointing to the next member of a JSON object or JSON array, or 0 in case the JSON object or JSON array has no more members.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY.
- Parameter 'iter' is an iterator pointing to a member of parameter 'json_value'.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
