# sjv.date()

## Syntax:
`#include <bic_sjv>`
`function string sjv.date( [ const string aspect,... ] )`

## Description
Indicates a JSON number is expected that contains a date value (expressed in number of days since 0001-01-01). By default, the date is optional (i.e., does not have to appear in the JSON), can also be 0, but may not be null. The following aspects can be specified:

- [sjv.min()](sjv.min.md)- specifies the minimum value allowed expressed in number of days since 0001-01-01

- [sjv.max()](sjv.max.md)- specifies the maximum value allowed expressed in number of days since 0001-01-01

- [sjv.required()](sjv.required.md)- specifies the date is required

- [sjv.nullable()](sjv.nullable.md)- specifies the date is nullable

- [sjv.filled()](sjv.filled.md)- specifies the date may not be 0

Example:
```

string  date.def(1) based
long    json
long    result

|* Define a JSON object with a 'date' JSON number that contains a date value greater than or equal to
|* 2024-01-01; the date is required
str.assign(date.def, sjv.object(sjv.fields(
   "date", sjv.date(sjv.min(date.to.num(2024, 1, 1)), sjv.required())
)))

|* json = { "date": 738917 }	= 2024-02-01
result = sjv.validate(json, date.def)
|* => result = 0

|* json = { "date": 738885 }	= 2023-12-31
result = sjv.validate(json, date.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root JSON value must be at least 738886 (2024-01-01)"

|* json = { "name": "john" }
result = sjv.validate(json, date.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "date is missing"
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
