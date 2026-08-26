# sjv.domain()

## Syntax:
`#include <bic_sjv>`
`function string sjv.domain( [ const string aspect, ... ] )`

## Description
Indicates a JSON value is expected that matches that datatype of the given domain. It is validated using the following properties of the domain:
- type (string, double, long, enum, date, utc, etc.)
- length
- legal and illegal characters
- range
- convert mode (uppercase, lowercase, none)
- enum keywords in case of an enum domain; applies to JSON string values; the string value must be one of the allowed enum keywords  By default, the value is optional (i.e., does not have to appear in the JSON), can also be empty ("", 0, 0.0), but may not be null. The following aspects can be specified:
- ` [sjv.min()](sjv.min.md)`- can be used to impose extra limitations besides what the domain specifies:
- for string types: specifies the minimum length in characters
- for numeric types: specifies the minimum allowed value
- does not apply to enum domains
- ` [sjv.max()](sjv.max.md)`- can be used to impose extra limitations besides what the domain specifies:
- for string types: specifies the maximum length in characters
- for numeric types: specifies the maximum allowed value
- does not apply to enum domains
- ` [sjv.required()](sjv.required.md)`- specifies the value is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the value is nullable
- ` [sjv.filled()](sjv.filled.md)`- specifies the value may not be "", 0.0 or 0   For string type domains you can also specify one of the following formats:
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

string  domain.def(1) based
long    json
long    result

|* Define an array having elements that conform to domain tccom.bpid; the elements must be filled
|* and only allow alphanumeric characters
str.assign(domain.def, sjv.array(sjv.domain("tccom.bpid", sjv.filled(), sjv.alphanum())))

|* json = [ "BP001", "BP002" ]
result = sjv.validate(json, domain.def)
|* => result = 0

|* json = [ "BP001", "BP_02" ]
result = sjv.validate(json, domain.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root[2] may only contain characters in the range [a-zA-Z0-9]"

|* json = [ "BP001", "" ]
result = sjv.validate(json, domain.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root[2] must be filled; an empty string is not allowed"

|* Define a JSON object having a "checked" field of type JSON string that conforms to
|* domain tcyesno and may be an empty string
str.assign(domain.def, sjv.object(sjv.fields(
   "checked", sjv.domain("tcyesno")
)))

|* json = { "checked": "yes" }
result = sjv.validate(json, domain.def)
|* => result = 0

|* json = { "checked": "" }
result = sjv.validate(json, domain.def)
|* => result = 0, empty string is allowed

|* json = { "checked": "xyz" }
result = sjv.validate(json, domain.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "root JSON value is outside its valid range; only the following values are allowed: yes, no"
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects the JSON value is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.nullable()](sjv.nullable.md), and [sjv.max()](sjv.max.md)  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
