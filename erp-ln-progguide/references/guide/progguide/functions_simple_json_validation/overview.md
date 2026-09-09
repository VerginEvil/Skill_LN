# Simple JSON Validation overview
The Simple JSON Validation (SJV) functionality makes it easy, simple and convenient to validate JSON values. The benefits of the SJV functions are:

- *Easy to use*: The checks that must be performed are programmed in a declarative way. Instead of focusing on how to check the JSON structure, you only have to define what the expected structure looks like and what aspects must be validated.

- *Consistent error messages*: The SJV functionality provides clear error messages telling why the JSON is not valid. By using the SJV functionality the same error messages are given for similar errors. Error messages are set using function [dal.set.error.message()](../functions_message_handling/dal.set.error.message.md)

- *Powerful validations*: The SJV functionality provides a variety of aspects of JSON values that can be checked. It also can be used for structures with nested objects and arrays.

- *Reusable definitions*: With the SJV functions you can create reusable definitions that can be used in other definitions to check JSON against.

Note  The SJV functionality is meant to perform *basic* validations, like checking the structure of a JSON document, the type of values, and some commonly used formats, like ISO8601 dates and datetimes, base64 and hex strings etc. Some more complex validations like checking if a value exists in a table in the database, or a file that must exist cannot be performed by means of the SJV functionality.

## Usage
The SJV functions are easy to use. For example:
```

result = sjv.validate(json, sjv.object(sjv.required(), sjv.fields(
   "code",      sjv.string(sjv.required(), sjv.filled(), sjv.alpha(), sjv.max(6)),
   "name",      sjv.string(sjv.nullable()),
   "birthdate", sjv.date(sjv.required(), sjv.nullable())
)))
```
This describes and validates a JSON object with 3 fields, a code, a name and a birthdate:

- 'code' is required, i.e., the key 'code' must appear in the JSON object, it must be a string of max 6 characters in the range a-zA-Z and the string must be filled/may not be empty;

- 'name' is optional, i.e., the key 'name' does not have to appear in the JSON object, but if it appears, then it must either be a string that also may be empty, or it must be null;

- 'birthdate' is required, but it may be null; if not null it must be a date value (a long value expressed in number of days since 0001-01-01) and, as the field does not have to be filled, the value 0 (i.e., the 'empty' value of a date) is allowed as well.

According to this definition, the following JSON objects are valid:
```

{
  "code": "JSMITH",     |* 6 chars in the range a-zA-Z
                        |* name is optional, so may be left out
  "birthdate": null     |* null is valid, as birthdate is nullable
}
```
```

{
  "code": "JSMITH",
  "birthdate": 0        |* 0 is valid, as birthdate does not have to be 'filled'
}
```
```

{
  "code": "JSMITH",
  "birthdate": 726942   |* i.e. 1991-04-20, which is a valid date value
}
```
```

{
  "code": "JSMITH",
  "name": null,         |* name is nullable
  "birthdate": null
}
```
```

{
  "code": "JSMITH",
  "name": "",           |* name does not have to be filled
  "birthdate": null
}
```
```

{
  "code": "JSMITH",
  "name": "John Smith",
  "birthdate": 726942,
  "new_field": true     |* NOTE: new_field is not checked, as it is not part of the definition
}
```
The following JSON objects are invalid:
```

{
  "code": "JOHNSMITH",  |* dal error message set: "code must have at most 6 characters"
  "birthdate": null
}
```
```

{
  "code": "",           |* dal error message set: "code must be filled; an empty string is not allowed"
  "birthdate": 0
}
```
```

{
                        |* dal error message set: "code is missing"
  "birthdate": 726942
}
```
```

{
  "code": "JSMITH",
  "name": true,         |* dal error message set: "name must be a JSON string"
  "birthdate": null
}
```
```

{
  "code": "JSMITH",
  "birthdate": -1       |* dal error message set: birthdate must be in the range 1..3652059 (0001-01-01..9999-12-31)
}
```

## Related topics
- [Simple JSON Validation synopsis](synopsis.md)

- [Simple JSON Validation examples](examples.md)
