# sjv.tuple()

## Syntax:
`#include <bic_sjv>`
`function string sjv.tuple( const string aspect, ... )`

## Description
Indicates a JSON array is expected with a fixed length and of which the elements can have different types. By default, the array is optional (i.e., it does not have to appear in the JSON), but may not be null. The following aspects can be specified:
- ` [sjv.required()](sjv.required.md)`- specifies the array is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the array is nullable   You can specify the type of the individual elements using the following functions:
- ` [sjv.string()](sjv.string.md)`- the element is a JSON string
- ` [sjv.long()](sjv.long.md)`- the element is a JSON number containing a long value
- ` [sjv.double()](sjv.double.md)`- the element is a JSON number containing a double value
- ` [sjv.boolean()](sjv.boolean.md)`- the element is a JSON boolean
- ` [sjv.date()](sjv.date.md)`- the element is a JSON number containing a date value expressed in days since 0001-01-01
- ` [sjv.utc()](sjv.utc.md)`- the element is a JSON number containing a UTC value expressed in seconds since 1970-01-01 00:00:00 UTC
- ` [sjv.object()](sjv.object.md)`- the element is a JSON object
- ` [sjv.tuple()](sjv.tuple.md)`- the element is a JSON array of which all elements have the same type
- ` [sjv.tuple()](sjv.tuple.md)`- the element is a JSON array of fixed length is expected of which the elements may be of different types
- ` [sjv.domain()](sjv.domain.md)`- the element is a JSON value that has a type that is in accordance with the type of the domain   Example:
```

string  tuple.def(1) based
long    json
long    result

|* Define a JSON array with 3 elements:
|* - a string of format UUID that must be filled
|* - a long
|* - a nullable UTC value
str.assign(tuple.def, sjv.tuple(
   sjv.string(sjv.filled(), sjv.uuid()),
   sjv.double(),
   sjv.utc(sjv.nullable())
))

|* json = [
|*   "ebdd177b-28ed-4069-be23-3a7eb15cc5a6",
|*   12,
|*   1704087000    |* 2024-01-01T06:30:00+01:00
|* ]
result = sjv.validate(json, tuple.def)
|* => result = 0

|* json = [
|*   "ebdd177b-28ed-4069-be23-3a7eb15cc5a6",
|*   1704087000    |* 2024-01-01T06:30:00+01:00
|* ]
result = sjv.validate(json, tuple.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must have exactly 3 elements"

|* json = [
|*   "ebdd177b-28ed-4069-be23-3a7eb15cc5a6",
|*   12.56,
|*   1704087000    |* 2024-01-01T06:30:00+01:00
|* ]
result = sjv.validate(json, tuple.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[2] must be an integer value"
```

## Arguments
| | | |
|---|---|---|
| `const string` | `aspect, ...` |  a list of aspects and a type for each element in the tuple; e.g., [sjv.string()](sjv.string.md), [sjv.double()](sjv.double.md), etc.  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
