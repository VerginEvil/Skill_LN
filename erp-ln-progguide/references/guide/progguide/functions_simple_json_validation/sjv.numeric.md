# sjv.numeric()

## Syntax:
`#include <bic_sjv>`
`function string sjv.numeric( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string only contains characters in the range [0-9].
Example:
```

string  numeric.def(1) based
long    json
long    result

|* Define a JSON array with string elements that contain only numeric characters
str.assign(numeric.def, sjv.array(sjv.string(sjv.numeric())))

|* json = [ "1536", "957" ]
result = sjv.validate(json, numeric.def)
|* => result = 0

|* json = [ "-1536", "957" ]       |* minus sign is not allowed
result = sjv.validate(json, numeric.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value may only contain characters in the range [0-9]"

|* json = [ "1536", "957", "34c" ] |* c is not allowed
result = sjv.validate(json, numeric.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[3] may only contain characters in the range [0-9]"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string may only contain characters in the range [0-9]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
