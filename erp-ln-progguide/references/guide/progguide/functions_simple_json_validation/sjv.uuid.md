# sjv.uuid()

## Syntax:
`#include <bic_sjv>`
`function string sjv.uuid( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string contains a UUID, like `963bb6ef-de70-4812-8e4c-10cb1c966c26.`
Example:
```

string  uuid.def(1) based
long    json
long    result

|* Define a JSON array that contains UUIDs
str.assign(uuid.def, sjv.array(sjv.string(sjv.uuid())))

|* json = [ "963bb6ef-de70-4812-8e4c-10cb1c966c26" ]
result = sjv.validate(json, uuid.def)
|* => result = 0

|* json = [ "963bb6ef-de70-4812-8e4c-10cb1c966c26", "963bb6ef-ABCD-4812-8e4c-10cb1c966c26" ]
result = sjv.validate(json, uuid.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[2] is not a UUID string"

|* json = [ "963bb6ef-de70-4812-8e4c-10cb1c966c26", "963bb6ef-8e4c-10cb1c966c26" ]
result = sjv.validate(json, uuid.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[2] is not a UUID string"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string be a UUID

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
