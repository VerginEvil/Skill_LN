# Json.iterKey()

## Syntax:
`#include <bic_json>`
`function string Json.iterKey( long json_object, long iter )`

## Description
Returns the key name to which the specified iterator is pointing.

## Arguments
| | | |
|---|---|---|
| `long` | `json_object` |  A JSON object.  |
| `long` | `iter` |  A JSON iterator.  |

## Return values
The key name to which the specified iterator is pointing.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_object' is a JSON value of type JSON_TYPE_OBJECT.
- Parameter 'iter' is an iterator pointing to a member of parameter 'json_object'.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
