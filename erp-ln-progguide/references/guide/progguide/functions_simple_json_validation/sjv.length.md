# sjv.length()

## Syntax:
`#include <bic_sjv>`
`function string sjv.length( long length )`

## Description
Specifies an exact length in characters (for strings) or an exact number of elements (for arrays).
Example:
```

string  length.def(1) based
long    json
long    result

|* Define a JSON array with string elements having at most 3 characters
str.assign(length.def, sjv.array(sjv.string(sjv.length(3))))

|* json = [ "abc", "123" ]
result = sjv.validate(json, length.def)
|* => result = 0

|* json = [ "abcd", "123" ]
result = sjv.validate(json, length.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "root[1] must have at most 3 characters"

|* Define a JSON array with exactly 2 elements of type long
str.assign(length.def, sjv.array(sjv.length(2), sjv.long()))

|* json = [ 20, 21 ]
result = sjv.validate(json, length.def)
|* => result = 0

|* json = [ 20 ]
result = sjv.validate(json, length.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root JSON value must have exactly 2 elements"
```

## Arguments
| | | |
|---|---|---|
| `long` | `length` |  a length or number of elements  |

## Return values
a definition string that specifies the length of a JSON string value or the number of elements of a JSON array

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
