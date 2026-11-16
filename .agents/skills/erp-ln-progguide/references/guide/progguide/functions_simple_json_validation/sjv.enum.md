# sjv.enum()

## Syntax:
`#include <bic_sjv>`
`function string sjv.enum( const string value,... )`

## Description
Indicates a list of allowed values of a JSON string. Use this if an enum domain cannot be used.
Example:
```

string  enum.def(1) based
long    json
long    result

|* Define a JSON object with a 'switch' field with 2 possible values, on and off.
str.assign(enum.def, sjv.object(sjv.fields(
   "switch", sjv.string(sjv.enum("on", "off"))
)))

|* json = { "switch": "on" }
result = sjv.validate(json, enum.def)
|* => result = 0

|* json = { "switch": "OFF" }
result = sjv.validate(json, enum.def)
|* => result = SJV_OUT_OF_RANGE
|* dal error message set: "switch is outside its valid range; only the following values are allowed: on, off"
```

## Arguments
| | | |
|---|---|---|
| `const string` | `value,...` |  a list of allowed values  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
