# sjv.hex()

## Syntax:
`#include <bic_sjv>`
`function string sjv.hex( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string only contains HEX encoded data. A valid HEX encoded string has a length that is divisible by 2 and only contains characters in the range [a-fA-F0-9].
Example:
```

string  hex.def(1) based
long    json
long    result

|* Define a JSON object with a 'color' field that contains a hex encoded string of 6 chars
str.assign(hex.def, sjv.object(sjv.fields(
   "color": sjv.string(sjv.hex(), sjv.length(6))
)))

|* json = { "color": "FF00FF" }
result = sjv.validate(json, hex.def)
|* => result = 0

|* json = { "color": "FF00KK" }
result = sjv.validate(json, hex.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "color is not a hex string"

|* json = { "color": "FF0FF" }	|* not a multiple of 2
result = sjv.validate(json, hex.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "color is not a hex string"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be a HEX encoded string

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
