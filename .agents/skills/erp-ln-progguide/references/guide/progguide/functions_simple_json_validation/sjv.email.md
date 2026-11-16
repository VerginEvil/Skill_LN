# sjv.email()

## Syntax:
`#include <bic_sjv>`
`function string sjv.email( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string contains an email address. An email address is considered valid if:

- it has the format local-part@domain-part;

- the local-part (the part before the @) is not empty;

- the domain-part (the part after the @) is not empty, contains at least one dot, does not start with a dot and does not end with a dot.

Example:
```

string  email.def(1) based
long    json
long    result

|* Define a JSON object with an email field
str.assign(email.def, sjv.object(sjv.fields(
   "email", sjv.string(sjv.email())
)))

|* json = { "email": "info@example.com" }
result = sjv.validate(json, email.def)
|* => result = 0

|* json = { "email": "@example.com" }
result = sjv.validate(json, email.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "email is not a valid email address"

|* json = { "email": "info@example." }
result = sjv.validate(json, email.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "email is not a valid email address"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be a valid email address

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)

- [Synopsis](synopsis.md)

- [Examples](examples.md)

- [sjv.validate()](sjv.validate.md)
