# sjv.utc()

## Syntax:
`#include <bic_sjv>`
`function string sjv.utc( [ const string aspect, ... ] )`

## Description
Indicates a JSON number is expected that contains a UTC value (expressed in seconds since 1970-01-01 00:00:00 UTC). By default, the UTC value is optional (i.e., does not have to appear in the JSON), can also be 0 (1970-01-01 00:00:00 UTC), but may not be null. The following aspects can be specified:
- ` [sjv.min()](sjv.min.md)`- specifies the minimum value allowed expressed in seconds since 1970-01-01 00:00:00 UTC
- ` [sjv.max()](sjv.max.md)`- specifies the maximum value allowed expressed in seconds since 1970-01-01 00:00:00 UTC
- ` [sjv.required()](sjv.required.md)`- specifies the UTC value is required
- ` [sjv.nullable()](sjv.nullable.md)`- specifies the UTC valueis nullable
- ` [sjv.filled()](sjv.filled.md)`- specifies the UTC value may not be 0 (i.e., 1970-01-01 00:00:00 UTC)   Example:
```

string  utc.def(1) based
long    json
long    result

|* Define a JSON object having an 'archived_at' field that contains a UTC value greater than 1970-01-01 00:00:00
|* and is at max 2049-12-31 23:59:59 UTC; also, the UTC value is not required to appear in the JSON
str.assign(utc.def, sjv.object(sjv.fields(
   "archived_at", sjv.utc(sjv.filled(), sjv.max(iso.to.utc("2049-12-31T23:59:59Z")))
)))

|* json = { "archived_at": 1705756516 }   |* 2024-01-20T14:15:16+01:00
result = sjv.validate(json, utc.def)
|* => result = 0

|* json = { "archived_at": 0 }            |* 1970-01-01T00:00:00Z
result = sjv.validate(json, utc.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "archived_at must be filled; 0 is not allowed"

|* json = { "archived_at": 4070905200 }   |* 2099-01-01T00:00:00+01:00
result = sjv.validate(json, utc.def)
|* => result = SJV_ERR_OUT_OF_RANGE
|* dal error message set: "archived_at must be at most 2524607999 (2049-12-31T23:59:59Z)"

|* json = { "id": 123 }
result = sjv.validate(json, utc.def)
|* => result = 0, as the archived_at value is not required
```

## Arguments
| | | |
|---|---|---|
| `[ const string` | `aspect, ... ]` |  a list of aspects the JSON number is expected to have; e.g., [sjv.required()](sjv.required.md), [sjv.nullable()](sjv.nullable.md), and [sjv.max()](sjv.max.md)  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
