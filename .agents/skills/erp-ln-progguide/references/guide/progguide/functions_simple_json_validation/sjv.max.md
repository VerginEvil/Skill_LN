# sjv.max()

## Syntax:
`#include <bic_sjv>`
`function string sjv.max( [ long|double value ] )`

## Description
Specifies a maximum value, length or number of elements.

- For strings: specifies the expected maximum length in characters.

- For arrays: specifies the expected maximum number of elements.

- For longs and doubles: specifies the expected maximum value.

- For dates: specifies the expected maximum value, pass a long expressing the date in days since 0001-01-01.

- For UTC values: specifies the expected maximum value, pass a long expressing the UTC value in seconds since 1970 UTC.

Example:
```

string  max.def(1) based
long    json
long    result

|* Define a JSON array with elements of at most 3 characters
str.assign(max.def, sjv.array(sjv.string(sjv.max(3))))

|* json = [ "abc", "def" ]
result = sjv.validate(json, max.def)
|* => result = 0

|* json = [ "abcd", "def" ]
result = sjv.validate(json, max.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "root[1] must have at most 3 characters"

|* Define a JSON object with a date field with a maximum date of 2023-12-31
str.assign(max.def, sjv.object(sjv.fields(
   "date", sjv.date(sjv.max(date.to.num(2023, 12, 31)))
)))

|* json = { "date": 738884 }	= 2023-12-30
result = sjv.validate(json, max.def)
|* => result = 0

|* json = { "date": 738917 }	= 2024-02-01
result = sjv.validate(json, max.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "root JSON value must be at most 738885 (2023-12-31)"

|* Define a JSON array with at most 2 elements of type any
str.assign(max.def, sjv.array(sjv.max(2), sjv.any()))

|* json = [ "hello", 1.23 ]
result = sjv.validate(json, max.def)
|* => result = 0

|* json = [ "hello", 1.23, true ]
result = sjv.validate(json, max.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must have at most 2 elements"
```

## Arguments
| | | |
|---|---|---|
| `[ long|double` | `value ]` |  a maximum value, length or number of elements  |

## Return values
a definition string that tells the maximum value of a JSON number, or the maximum length of a JSON string or the maximum number of elements of a JSON array

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
