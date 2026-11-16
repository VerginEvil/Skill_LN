# sjv.double()

## Syntax:
`#include <bic_sjv>`
`function string sjv.double( [ const string aspect,... ] )`

## Description
Indicates a JSON number is expected that contains a double value. By default, the double is optional (i.e., does not have to appear in the JSON), can be any value, including 0.0, but may not be null. The following aspects can be specified:

- [sjv.min()](sjv.min.md)- specifies the minimum value allowed

- [sjv.max()](sjv.max.md)- specifies the maximum value allowed

- [sjv.required()](sjv.required.md)- specifies the double is required

- [sjv.nullable()](sjv.nullable.md)- specifies the double is nullable

- [sjv.filled()](sjv.filled.md)- specifies the double may not be 0.0

Example:
```

string  double.def(1) based
long    json
long    result

|* Define a JSON array consisting of 2 JSON numbers between 100.0 and 119.99; null is also allowed
str.assign(double.def, sjv.array(sjv.length(2), sjv.double(sjv.min(100.0), sjv.max(119.99), sjv.nullable())))

|* json = [ 109.23, 114.49 ]
result = sjv.validate(json, double.def)
|* => result = 0

|* json = [ 109.23, null ]
result = sjv.validate(json, double.def)
|* => result = 0, null is allowed

|* json = [ 109.23, 145.32 ]
result = sjv.validate(json, double.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root[2] must be at most 119.99"
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
