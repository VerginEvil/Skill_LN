# Json.iterValue()

## Syntax:
`#include <bic_json>`
`function long Json.iterValue( long json_value, long iter )`

## Description
Returns the JSON value to which the specified iterator is pointing.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON object or array.  |
| `long` | `iter` |  A JSON iterator.  |

## Return values
The JSON value to which the specified iterator is pointing.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY.
- Parameter 'iter' is an iterator pointing to a member of parameter 'json_value'.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
