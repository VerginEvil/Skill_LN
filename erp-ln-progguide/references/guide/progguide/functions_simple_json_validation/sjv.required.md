# sjv.required()

## Syntax:
`#include <bic_sjv>`
`function string sjv.required( )`

## Description
Indicates the JSON value must be present. If the JSON value is the root value, the JSON handle may not be 0. If the JSON value is associated with a key in a JSON object, its key must be present.
Example:
```

string  required.def(1) based
long    json
long    result

|* Define a JSON object with a required id field of type string
str.assign(required.def, sjv.object(sjv.fields(
   "id", sjv.string(sjv.required())
))

|* json = { "id": "abc123" }
result = sjv.validate(json, required.def)
|* => result = 0

|* json = { "city": "New York" }
result = sjv.validate(json, required.def)
|* => result = SJV_ERR_INVALID_ARG
|* dal error message set: "id is missing"
```

## Return values
a definition string that tells a JSON value is required, i.e., must appear in the JSON document

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
