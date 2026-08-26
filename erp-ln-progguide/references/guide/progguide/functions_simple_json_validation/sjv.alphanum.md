# sjv.alphanum()

## Syntax:
`#include <bic_sjv>`
`function string sjv.alphanum( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string only contains characters in the range [a-zA-Z0-9].
Example:
```

string  alphanum.def(1) based
long    json
long    result

|* Define a JSON array having string elements containing only characters in the range [a-zA-Z0-9]
str.assign(alphanum.def, sjv.array(sjv.string(sjv.alphanum()))

|* json = [ "Abc123", "45dEf" ]
result = sjv.validate(json, alphanum.def)
|* => result = 0

|* json = [ "Abc123+zyx", "45dEf" ]
result = sjv.validate(json, alphanum.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[1] may only contain characters in the range [a-zA-Z0-9]"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string may only contain characters in the range [a-zA-Z0-9]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
