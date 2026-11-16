# sjv.fields()

## Syntax:
`#include <bic_sjv>`
`function string sjv.fields( const string name1, const string type1, [ const string name2, const string type2,... ] )`

## Description
Defines one or more fields of a JSON object. Each field has a name followed by a type. The following field types can be specified:

- [sjv.string()](sjv.string.md)- the field is a JSON string

- [sjv.long()](sjv.long.md)- the field is a JSON number containing a long value

- [sjv.double()](sjv.double.md)- the field is a JSON number containing a double value

- [sjv.boolean()](sjv.boolean.md)- the field is a JSON boolean

- [sjv.date()](sjv.date.md)- the field is a JSON number containing a date value expressed in days since 0001-01-01

- [sjv.utc()](sjv.utc.md)- the field is a JSON number containing a UTC value expressed in seconds since 1970-01-01 00:00:00 UTC

- [sjv.object()](sjv.object.md)- the field is a JSON object

- [sjv.array()](sjv.array.md)- the field is a JSON array of which all elements have the same type

- [sjv.tuple()](sjv.tuple.md)- the field is a JSON array of fixed length and of which the elements may be of different types

- [sjv.domain()](sjv.domain.md)- the field is a JSON value that has a type that is in accordance with the type of the domain

Example:
```

string  object.def(1) based
long    json
long    result

|* Define a JSON object with 6 fields of different types:
str.assign(object.def, sjv.object(sjv.fields(
   "code",      sjv.string(sjv.alpha(), sjv.max(3), sjv.required(), sjv.filled()),
   "descr",     sjv.domain("ttdesc35", sjv.nullable()),
   "color",     sjv.string(sjv.enum("red", "green", "yellow"), sjv.filled()),
   "factor",    sjv.double(sjv.nullable()),
   "homepage",  sjv.string(sjv.url()),
   "timestamp", sjv.string(sjv.isodatetime(), sjv.required())
)))

|* json = {
|*  "code": "ABC",
|*  "descr": "ABC Test",
|*  "color": "red",
|*  "factor": 0.5,
|*  "homepage": "http://www.infor.com",
|*  "timestamp": "2024-02-08T14:30:20Z"
|* }
result = sjv.validate(json, object.def)
|* => result = 0

|* json = {
|*  "code": "ABC",
|*  "descr": "ABC Test",
|*  "color": "red",
|*  "factor": true,
|*  "homepage": "http://www.infor.com",
|*  "timestamp": "2024-02-08T14:30:20Z"
|* }
result = sjv.validate(json, object.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "factor must be a JSON number"

|* json = {
|*  "code": "ABC",
|*  "descr": "ABC Test Test Test Test Test Test Test Test Test Test",
|*  "color": "red",
|*  "factor": 0.5,
|*  "homepage": "http://www.infor.com",
|*  "timestamp": "2024-02-08T14:30:20Z"
|* }
result = sjv.validate(json, object.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "descr is too long; no more than 35 characters allowed"
```

## Arguments
| | | |
|---|---|---|
| `const string` | `name1` |  the name of the first field  |
| `const string` | `type1` |  the type definition of the first field; e.g., [sjv.string()](sjv.string.md), [sjv.double()](sjv.double.md), [sjv.double()](sjv.double.md), etc.  |
| `[ const string` | `name2 ]` |  the name of the second field  |
| `[ const string` | `type2 ]` |  the type definition of the second field; e.g., [sjv.string()](sjv.string.md), [sjv.double()](sjv.double.md), [sjv.double()](sjv.double.md), etc.  |
| `[` | `... ]` |  combinations of name and type of other fields  |

## Return values
a definition string to build a JSON validation definition that can be passed to [sjv.validate()](sjv.validate.md)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
