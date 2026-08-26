# Json.copyToProcess()

## Syntax:
`#include <bic_json>`
`function long Json.copyToProcess( long json_value, long process_id )`

## Description
Returns a (deep) copy of a JSON value. The copy is created in the address space of the specified process. If this is another process than the current process, then the JSON is readonly for the current process. In case the JSON value is of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY, all contained members are copied as well.

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON value.  |
| `long` | `process_id` |  a process ID.  |

## Return values
A (deep) copy of the passed JSON value.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value.
- Parameter 'process_id' is greater than 0.

## Related topics
- [JSON overview](JSon_object_overview.md)
- [JSON synopsis](synopsis.md)
