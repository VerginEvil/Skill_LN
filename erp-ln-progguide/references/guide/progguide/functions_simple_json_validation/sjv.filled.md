# sjv.filled()

## Syntax:
`#include <bic_sjv>`
`function string sjv.filled( )`

## Description
Indicates the JSON value is expected to be filled. That is, the 'empty' value of a type ("", 0, 0.0, false, etc.) is not allowed.
Example:
```

string  filled.def(1) based
long    json
long    result

|* Define a JSON array having JSON strings that must be filled
str.assign(filled.def, sjv.array(sjv.string(sjv.filled()))

|* json = [ "ok", "nice" ]
result = sjv.validate(json, filled.def)
|* => result = 0

|* json = [ "ok", "" ]
result = sjv.validate(json, filled.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root[2] must be filled; an empty string is not allowed"
```

## Return values
a definition string that tells a JSON value must be filled, i.e., may not be empty

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
