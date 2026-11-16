# sjv.array()

## Syntax:
`#include <bic_sjv>`
`function string sjv.array( [ const string aspect,... ] )`

## Description
Indicates a JSON array is expected of which all elements have the same type. By default, the array is optional (i.e., it does not have to appear in the JSON), but may not be null. The following aspects can be specified:

- [sjv.length()](sjv.length.md)- the array is expected to have the exact number of elements

- [sjv.min()](sjv.min.md)- the array is expected to have at least this number of elements

- [sjv.max()](sjv.max.md)- the array is expected to have at most this number of elements

- [sjv.required()](sjv.required.md)- specifies the array is required

- [sjv.nullable()](sjv.nullable.md)- specifies the array is nullable

You can specify the type of the elements using one of the following functions:

- [sjv.string()](sjv.string.md)- each element is a JSON string

- [sjv.long()](sjv.long.md)- each element is a JSON number containing a long value

- [sjv.double()](sjv.double.md)- each element is a JSON number containing a double value

- [sjv.boolean()](sjv.boolean.md)- each element is a JSON boolean

- [sjv.date()](sjv.date.md)- each element is a JSON number containing a date value expressed in days since 0001-01-01

- [sjv.utc()](sjv.utc.md)- each element is a JSON number containing a UTC value expressed in seconds since 1970-01-01 00:00:00 UTC

- [sjv.object()](sjv.object.md)- each element is a JSON object

- [sjv.array()](sjv.array.md)- each element is a JSON array of which all elements have the same type

- [sjv.tuple()](sjv.tuple.md)- each element is a JSON array of fixed length and of which the elements may be of different types

- [sjv.domain()](sjv.domain.md)- each element is a JSON value that has a type that is in accordance with the type of the domain

Example:
```

string  array.def(1) based
long    json
long    result

|* Define a JSON array containing exactly 3 nullable longs; the array itself is not nullable
str.assign(array.def, sjv.array(sjv.length(3), sjv.long(sjv.nullable())))

|* json = [ 100, 101, null ]
result = sjv.validate(json, array.def)
|* => result = 0

|* json = [ 100, 101, "102" ]
result = sjv.validate(json, array.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[3] must be a JSON number"

|* json = [ 100, 101 ]
result = sjv.validate(json, array.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must have exactly 3 elements"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect,... ]` |  a list of aspects (including the type of the elements) the array is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.string()](sjv.string.md), etc.  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
