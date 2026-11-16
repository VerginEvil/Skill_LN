# sjv.alpha()

## Syntax:
`#include <bic_sjv>`
`function string sjv.alpha( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string only contains characters in the range [a-zA-Z].
Example:
```

string  alpha.def(1) based
long    json
long    result

|* Define a JSON array having string elements containing only characters in the range [a-zA-Z]
str.assign(alpha.def, sjv.array(sjv.string(sjv.alpha()))

|* json = [ "Abc", "dEf" ]
result = sjv.validate(json, alpha.def)
|* => result = 0

|* json = [ "Abc", "234" ]
result = sjv.validate(json, alpha.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "root[2] may only contain characters in the range [a-zA-Z]"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string may only contain characters in the range [a-zA-Z]

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
