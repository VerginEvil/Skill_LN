# sjv.isodate()

## Syntax:
`#include <bic_sjv>`
`function string sjv.isodate( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string contains an ISO 8601 date, like "2023-12-09".
Example:
```

string  isodate.def(1) based
long    json
long    result

|* Define a JSON array with at least 2 ISO 8601 date strings
str.assign(isodate.def, sjv.array(sjv.min(2), sjv.string(sjv.isodate())))

|* json = [ "2023-11-01", "2023-11-31"]
result = sjv.validate(json, isodate.def)
|* => result = 0

|* json = [ "2023-11-01", "11/31/2023"]
result = sjv.validate(json, isodate.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[2] is not a valid ISO8601 date"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be a datetime in ISO8601 format

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
