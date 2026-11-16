# sjv.min()

## Syntax:
`#include <bic_sjv>`
`function string sjv.min( [ long|double value ] )`

## Description
Specifies a minimum value, length or number of elements.

- For strings: specifies the expected minimum length in characters.

- For arrays: specifies the expected minimum number of elements.

- For longs and doubles: specifies the expected minimum value.

- For dates: specifies the expected minimum value, pass a long expressing the date in days since 0001-01-01.

- For UTC values: specifies the expected minimum value, pass a long expressing the UTC value in seconds since 1970 UTC.

Example:
```

string  min.def(1) based
long    json
long    result

|* Define a JSON array with elements of at least 3 characters
str.assign(min.def, sjv.array(sjv.string(sjv.min(3))))

|* json = [ "abc", "def", "ghi", "jkl" ]
result = sjv.validate(json, min.def)
|* => result = 0

|* json = [ "abc", "de" ]
result = sjv.validate(json, min.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "root[2] must have at least 3 characters"

|* Define a JSON object with a date field with a minimum date of 2024-01-01
str.assign(min.def, sjv.object(sjv.fields(
   "date", sjv.date(sjv.min(date.to.num(2024, 1, 1)))
)))

|* json = { "date": 738887 }	= 2024-01-02
result = sjv.validate(json, min.def)
|* => result = 0

|* json = { "date": 738885 }	= 2023-12-31
result = sjv.validate(json, min.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "root JSON value must be at least 738886 (2024-01-01)"

|* Define a JSON array with at least 2 elements of type any
str.assign(min.def, sjv.array(sjv.min(2), sjv.any()))

|* json = [ "hello", 1.23, null ]
result = sjv.validate(json, min.def)
|* => result = 0

|* json = [ "hello" ]
result = sjv.validate(json, min.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must have at least 2 elements"
```

## Arguments
| | | |
|---|---|---|
| `[ long|double` | `value ]` |  a minimum value, length or number of elements  |

## Return values
a definition string that tells the minimum value of a JSON number, or the minimum length of a JSON string or the minimum number of elements of a JSON array

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
