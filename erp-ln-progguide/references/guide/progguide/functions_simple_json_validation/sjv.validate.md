# sjv.validate()

## Syntax:
`#include <bic_sjv>`
`function long sjv.validate( long json, const string definition )`

## Description
Validates a JSON value according to the given definition. Use functions like [sjv.object()](sjv.object.md), [sjv.fields()](sjv.fields.md), [sjv.string()](sjv.string.md), etc. to build the definition.
Example:
```

string  employee.def(1) based
long    employee.json
long    result

|* Define an employee as a required JSON object with 4 properties:
|* - id, a required long that may not be 0;
|* - name, a required string that must be filled
|* - salary, an optional double that may be null
|* - active, a optional boolean
str.assign(employee.def, sjv.object(sjv.required(), sjv.fields(
   "id",     sjv.long(sjv.required(), sjv.filled()),
   "name",   sjv.string(sjv.required(), svj.filled()),
   "salary", sjv.double(sjv.nullable()),
   "active", sjv.boolean()
)))

|* employee.json = {
|*   "id": 123,
|*   "name": "Jane",
|*   "salary": 29786.34,
|*   "active": true
|* }
result = sjv.validate(employee.json, employee.def)
|* => result = 0

|* employee.json = {
|*   "id": 123,
|*   "salary": 29786.34,
|*   "active": true
|* }
result = sjv.validate(employee.json, employee.def)
|* => result = SJV_ERR_INVALID_ARGUMENT
|* dal error message set: "name is missing"
```

## Arguments
| | | |
|---|---|---|
| `long` | `json` |  the JSON value to validate  |
| `const string` | `definition` |  a definition built with sjv functions like [sjv.object()](sjv.object.md), [sjv.fields()](sjv.fields.md), [sjv.string()](sjv.string.md), etc.  |

## Return values
| | |
|---|---|
| 0 | The JSON is valid |
| SJV_ERR_INVALID_ARGUMENT (20004001) | The JSON structure is not according to the given definition; e.g., a required field is missing, a field is of the wrong type, etc.  |
| SJV_ERR_OUT_OF_RANGE (20004002) | A JSON value is not according to the given definition; e.g., a string value is empty but must be filled |
| SJV_ERR_INTERNAL (20005001) | The passed definition is not correct; 'internal' means that this is a programming error that must be fixed by the caller of this function.  |
Notes
- In all error cases a DAL error message has been set.
- An error code can be easily converted to HTTP status code as follows: `statuscode = (sjv.error \ 10000) / 10`. E.g. SJV_ERR_OUT_RANGE (20004001) becomes HTTP status code 400 (Bad Request) and SJV_ERR_INTERNAL becomes 500 (Internal Server Error)

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Related topics
- [Overview](overview.md)
- [Synopsis](synopsis.md)
- [Examples](examples.md)
