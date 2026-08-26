# sjv.string()

## Syntax:
`#include <bic_sjv>`
`function string sjv.string( [ const string aspect, ... ] )`

## Description
Indicates a JSON string is expected. By default, the string is optional (i.e., it does not have to appear in the JSON), may be of any length, including a length of zero characters (i.e. an empty string), but may not be null. The following aspects can be specified:
- ` [sjv.length()](sjv.length.md)`- specifies the exact length in characters
- ` [sjv.min()](sjv.min.md)`- specifies the minimum length in characters
- ` [sjv.max()](sjv.max.md)`- specifies the maximum length in characters
- ` [sjv.required()](sjv.required.md)`- specifies the string is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the string is nullable
- ` [sjv.filled()](sjv.filled.md)`- specifies the string may not be an empty string
- ` [sjv.enum()](sjv.enum.md)`- specifies a list of allowed values   You can also specify one of the following formats:
- ` [sjv.alpha()](sjv.alpha.md)`- the string may only contain characters in the range [a-zA-Z]
- ` [sjv.alphanum()](sjv.alphanum.md)`- the string may only contain characters in the range [a-zA-Z0-9]
- ` [sjv.base64()](sjv.base64.md)`- the string must be a valid base64 encoded string
- ` [sjv.email()](sjv.email.md)`- the string must be a valid email address
- ` [sjv.hex()](sjv.hex.md)`- the string must be a valid HEX encoded string
- ` [sjv.isodate()](sjv.isodate.md)`- the string must be a date in ISO 8601 format
- ` [sjv.isodatetime()](sjv.isodatetime.md)`- the string must be a datetime in ISO 8601 format
- ` [sjv.numeric()](sjv.numeric.md)`- the string may only contain characters in the range [0-9]
- ` [sjv.url()](sjv.url.md)`- the string must be a valid url
- ` [sjv.uuid()](sjv.uuid.md)`- the string must be a valid UUID (or GUID) of 36 characters   Example:
```

string  string.def(1) based
long    json
long    result

|* Define a JSON object having a non-empty 'message' JSON string of max 6 alphanumeric
|* characters; the string is required (must appear in the JSON) and the string may not be null
str.assign(string.def, sjv.object(sjv.fields(
   "message", "sjv.string(sjv.max(6), sjv.alphanum(), sjv.filled(), sjv.required())
)))

|* json = { "message": "hello" }
result = sjv.validate(json, string.def)
|* => result = 0

|* json = { "message": "world!" }
result = sjv.validate(json, string.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "message may only contain characters in the range [a-zA-Z0-9]"

|* Define a JSON array with strings that have 3 possible values: red, green, blue
str.assign(string.def, sjv.array(sjv.string(sjv.enum("red", "green", "blue"))))

|* json = [ "red", "green" ]
result = sjv.validate(json, string.def)
|* => result = 0

|* json = [ "yellow", "blue" ]
result = sjv.validate(json, string.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root[1] is outside its valid range; only the following values are allowed: red, green, blue"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects and/or formats the string is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.nullable()](sjv.nullable.md), and [sjv.url()](sjv.url.md)  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
