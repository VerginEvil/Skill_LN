# sjv.base64()

## Syntax:
`#include <bic_sjv>`
`function string sjv.base64( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): Indicates the JSON field or element contains base64 encoded data. A valid base64 encoded string has a length that is divisible by 4, and only contains characters in the range [a-zA-Z0-9+/=].
Example:
```

string  base64.def(1) based
long    json
long    result

|* Define a JSON array with base64 encoded string elements
str.assign(base64.def, sjv.array(sjv.string(sjv.base64())))

|* json = [ "QQ==" ]    |* the character A
result = sjv.validate(json, base64.def)
|* => result = 0

|* json = [ "QQ=" ]     |* one = sign is missing
result = sjv.validate(json, base64.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[1] is not a base64 string"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be a base64 encoded string

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
