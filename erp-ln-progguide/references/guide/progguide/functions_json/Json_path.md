# Json.path()

## Syntax:
`#include <bic_json>`
`function long Json.path( long json_value, string|long... )`

## Description
Returns the JSON value in a JSON object or array, which is located at the specified path. The parameters passed to this function determine the path that is chosen to locate the JSON value. Example:
```

{
  "name": "John Doe",
  "phone numbers": [ "06-12345678", "0342-428888" ],
  "department": {
	"id": "HR",
    "name": "Human Resources",
    "office days": ["Monday", "Wednesday", "Friday"]
  }
}

|* To get the 2nd phone number:
phone2 = Json.path(obj, "phone numbers", 2)

|* To get the department name:
depname = Json.path(obj, "department", "name")

|* To get the value "Friday":
workday3 = Json.path(obj, "department", "office days", 3)
```

## Arguments
| | | |
|---|---|---|
| `long` | `json_value` |  A JSON object or array.  |
| `string|long` | `...` |  The key names and/or array indices which together form the path to a JSON value in the given JSON object or array.  |

## Return values
The JSON value requested.

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2120.

## Preconditions
- Parameter 'json_value' is a JSON value of type JSON_TYPE_OBJECT or JSON_TYPE_ARRAY.

- The combined parameters are a valid path in the JSON object or array.

## Related topics
- [JSON overview](JSon_object_overview.md)

- [JSON synopsis](synopsis.md)
