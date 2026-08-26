# Json.isNull

## Syntax:
`#include <bic_json>`
`function boolean Json.isNull( long json_value )`

## Description
Tests whether a JSON value is a JSON null value.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |

## Return values
*true* if the JSON value is of type JSON_TYPE_NULL, else *false*.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
