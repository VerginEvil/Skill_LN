# Json.delete()

## Syntax:
`#include <bic_json>`
`function void Json.delete( long json_value )`

## Description
Deletes a JSON value. In case the JSON value is of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY all contained members are deleted as well.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.
- Parameter 'json_value' is detached (i.e. it is not a member of a JSON object or JSON array).

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
