# sjv.object()

## Syntax:
`#include <bic_sjv>`
`function string sjv.object( [ const string aspect, ... ] )`

## Description
Indicates a JSON object is expected. By default, the object is optional (i.e., it does not have to appear in the JSON), but may not be null. The following aspects can be specified:
- ` [sjv.fields()](sjv.fields.md)`- specifies one or more fields
- ` [sjv.required()](sjv.required.md)`- specifies the object is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the object is nullable   Example:
```

string  object.def(1) based
long    json
long    result

|* Define a JSON object with 1 required and 1 optional field;
|* the JSON object itself is not required and may be null
str.assign(object.def, sjv.object(sjv.nullable(), sjv.fields(
   "user",   sjv.string(sjv.required()),
   "active", sjv.boolean()
)))

|* json = {
|*   "user": "john",
|*   "active": true
|* }
result = sjv.validate(json, object.def)
|* => result = 0

|* json = null
result = sjv.validate(json, object.def)
|* => result = 0

|* json = {
|*   "active": true
|* }
result = sjv.validate(json, object.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "user is missing"

|* json = [ "hi" ]
result = sjv.validate(json, object.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must be a JSON object"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects the object is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.fields()](sjv.fields.md), etc.  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
