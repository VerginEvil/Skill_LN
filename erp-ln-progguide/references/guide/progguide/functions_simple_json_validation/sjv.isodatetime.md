# sjv.isodatetime()

## Syntax:
`#include <bic_sjv>`
`function string sjv.isodatetime( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string contains an ISO 8601 datetime, like "2023-12-09T15:29:34Z" or "2023-12-09T16:29:34+01:00".
Example:
```

string  isodatetime.def(1) based
long    json
long    result

|* Define a JSON object with a 'order_date' that is an ISO8601 datetime string
str.assign(isodatetime.def, sjv.object(sjv.fields(
   "order_date", sjv.string(sjv.isodatetime())
)))

|* json = { "order_date": "2023-11-21T14:15:16Z" }
result = sjv.validate(json, isodatetime.def)
|* => result = 0

|* json = { "order_date": "2023-11-21 14:15:16Z" }  |* missing T
result = sjv.validate(json, isodatetime.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "order_date is not a valid ISO8601 datetime"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be a date in ISO8601 format

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
