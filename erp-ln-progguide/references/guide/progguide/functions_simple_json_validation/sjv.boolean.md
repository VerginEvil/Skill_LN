# sjv.boolean()

## Syntax:
`#include <bic_sjv>`
`function string sjv.boolean( [ const string aspect, ... ] )`

## Description
Indicates a JSON boolean is expected. By default, the boolean is optional (i.e., does not have to appear in the JSON), but may not be null. The following aspects can be specified:
- ` [sjv.required()](sjv.required.md)`- specifies the boolean is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the boolean is nullable
- ` [sjv.filled()](sjv.filled.md)`- specifies the boolean may not be false   Example:
```

string  boolean.def(1) based
long    json
long    result

|* Define a JSON object with an 'active' field of type boolean
str.assign(boolean.def, sjv.object(sjv.fields(
   "active", sjv.boolean()
)))

|* json = { "active": true }
result = sjv.validate(json, boolean.def)
|* => result = 0

|* json = { "active": null }
result = sjv.validate(json, boolean.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* DAL error message set: "active cannot be null"

|* json = { "active": 1 }
result = sjv.validate(json, boolean.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "active must be a JSON boolean"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects the JSON boolean is expected to have; e.g., [sjv.required()](sjv.required.md) and [sjv.nullable()](sjv.nullable.md)  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
