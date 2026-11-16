# sjv.long()

## Syntax:
`#include <bic_sjv>`
`function string sjv.long( [ const string aspect,... ] )`

## Description
Indicates a JSON number is expected that contains a long value. By default, the long is optional (i.e., does not have to appear in the JSON), can be any value, including 0, but may not be null. The following aspects can be specified:

- [sjv.min()](sjv.min.md)- specifies the minimum value allowed

- [sjv.max()](sjv.max.md)- specifies the maximum value allowed

- [sjv.required()](sjv.required.md)- specifies the long is required

- [sjv.nullable()](sjv.nullable.md)- specifies the long is nullable

- [sjv.filled()](sjv.filled.md)- specifies the long may not be 0

Example:
```

string  long.def(1) based
long    json
long    result

|* Define a JSON object with a field "z" of type JSON number, allowing only integer values
|* between -10 and 10, except 0
str.assign(long.def, sjv.object(sjv.fields(
   "z", sjv.long(sjv.min(-10), sjv.max(10), sjv.filled())
)))

|* json = { "z": 4 }
result = sjv.validate(json, long.def)
|* => result = 0

|* json = { "z": 0 }
result = sjv.validate(json, long.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* DAL error message set: "z must be filled; 0 is not allowed"

|* json = { "z": -11 }
result = sjv.validate(json, long.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "z must be at least -10"

|* json = { "z": 5.34 }
result = sjv.validate(json, long.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "z must be an integer value"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect,... ]` |  a list of aspects the JSON number is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.nullable()](sjv.nullable.md), and [sjv.max()](sjv.max.md)  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
