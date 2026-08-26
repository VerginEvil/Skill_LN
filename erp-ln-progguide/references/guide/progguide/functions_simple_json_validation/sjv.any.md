# sjv.any()

## Syntax:
`#include <bic_sjv>`
`function string sjv.any( [ const string aspect, ... ] )`

## Description
Indicates a JSON value is expected that can be of any type, including null. By default, the value is optional (i.e., does not have to appear in the JSON). The following aspect can be specified:
- ` [sjv.required()](sjv.required.md)`- specifies the value is required   Example:
```

string  any.def(1) based
long    json
long    result

|* Define a JSON objec having a required value that can be of any type
str.assign(any.def, sjv.object(sjv.fields(
   "value", sjv.any(sjv.required())
)))

|* json = { "value": true }
result = sjv.validate(json, any.def)
|* => result = 0

|* json = { "value": [ 1, 3 ] }
result = sjv.validate(json, any.def)
|* => result = 0

|* json = { "value": null }
result = sjv.validate(json, any.def)
|* => result = 0

|* json = { "id": 1 }
result = sjv.validate(json, any.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "value is missing"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects the JSON value is expected to have; currently only [sjv.required()](sjv.required.md) is supported  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
