# sjv.url()

## Syntax:
`#include <bic_sjv>`
`function string sjv.url( )`

## Description
Can be passed to [sjv.string()](sjv.string.md): indicates the JSON string contains a URL. A URL is considered valid if it has the following form: `http[s]://host[:port][/path][?query]`
Example:
```

string  url.def(1) based
long    json
long    result

|* Define a JSON object having a homepage field that must be a valid URL
str.assign(url.def, sjv.object(sjv.fields(
   "homepage", sjv.string(sjv.url())
)))

|* json = { "homepage": "http://www.infor.com/pages?search=home" }
result = sjv.validate(json, url.def)
|* => result = 0

|* json = { "homepage": "https://:8080/index.html" }
result = sjv.validate(json, url.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "homepage is not a valid URL"

|* json = { "homepage": "http://www.infor.com:100000/doc/ln" }
result = sjv.validate(json, url.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "homepage is not a valid URL"
```

## Return values
a definition string that can be passed to [sjv.string()](sjv.string.md) and defines that the string must be valid URL

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
- [sjv.validate()](sjv.validate.md)
