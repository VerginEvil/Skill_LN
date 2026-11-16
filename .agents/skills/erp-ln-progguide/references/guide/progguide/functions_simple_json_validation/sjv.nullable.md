# sjv.nullable()

## Syntax:
`#include <bic_sjv>`
`function string sjv.nullable( )`

## Description
Indicates the JSON value may be null.
Example:
```

string  nullable.def(1) based
long    json
long    result

|* Define a JSON object with a nullable id field of type string
str.assign(nullable.def, sjv.object(sjv.fields(
   "id", sjv.string(sjv.nullable())
))

|* json = { "id": "abc123" }
Json.setString(json, "id", "abc123")
result = sjv.validate(json, nullable.def)
|* => result = 0

|* json = { "id": null }
result = sjv.validate(json, nullable.def)
|* => result = 0

|* json = { "id": false }
result = sjv.validate(json, nullable.def)
|* => result = SJV_ERR_INVALID_ARG
|* dal error message set: "id must be a JSON string"
```

## Return values
a definition string that tells a JSON value may also be null

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
