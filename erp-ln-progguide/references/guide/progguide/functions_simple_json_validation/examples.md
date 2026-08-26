# Simple JSON Validation examples
This page gives examples of how to use the SJV (Simple JSON Validation) functions.

## Validating a complete JSON structure
Suppose we have the following JSON representing an item.
```

{
  "id": "ABC12345",
  "name": "ABC Bike",
  "type": "product",
  "supplier": {
    "name": "ACME_COMP",
    "address": {
      "street": "High Street",
      "number": 235,
      "zip_code": "1234AB"
    },
    "phone": "+31342799400",
    "email": "info@acme.com"
  },
  "price": {
    "value": 534.99,
    "currency": "EUR"
  },
  "packed": true,
  "home_currencies": [ "EUR", "USD", "AUD" ],
  "color": null,
  "active": false
}
```

## Validation rules
Suppose the following rules apply:
- The JSON document itself must be present, and it must be JSON object
- 'id' is a required string, must be filled (no empty string allowed), and may only contain alphanumeric characters
- 'name' is an optional, nullable string, but if present, it must be filled (no empty string allowed)
- 'type' is a required string, with 3 possible values: product, generic, tool
- 'supplier' is a required object, with the following properties:
- 'name' is required and must be according to domain 'tccom.bpid'
- 'address' is an optional, nullable object, with the following properties:
- 'street' is a required string
- 'number' is a required long
- 'zip_code' is an optional, nullable string and may only contain alphanumeric characters
- 'phone' is an optional, nullable string
- 'email' is an optional, nullable string and must contain a valid email address if filled
- 'price' is a required object, with the following properties:
- 'value' is required double
- 'currency' is a required string of max 3 characters and must be filled
- 'packed' is a required boolean
- 'home_currencies' is a required array with max 4 string elements, each of max 3 characters
- 'color' is a nullable string, with 4 possible values: red, blue, green, yellow
- 'active' is an optional boolean

## Validation rules in code
Validation of the aforementioned JSON value based on these rules can be programmed as follows:
```

#include <bic_sjv>

long    result

result = sjv.validate(json, sjv.object(sjv.required(), sjv.fields(
   "id",              sjv.string(sjv.required(), sjv.filled(), sjv.alphanum()),
   "name",            sjv.string(sjv.nullable(), sjv.filled()),
   "type",            sjv.string(sjv.required(), sjv.enum("product", "generic", "tool")),
   "supplier",        sjv.object(sjv.required(), sjv.fields(
      "name",         sjv.domain("tccom.bpid", sjv.required()),
      "address",      sjv.object(sjv.nullable(), sjv.fields(
         "street",    sjv.string(sjv.required()),
         "number",    sjv.long(sjv.required()),
         "zip_code",  sjv.string(sjv.nullable(), sjv.alphanum())
      )),
      "phone",        sjv.string(sjv.nullable()),
      "email",        sjv.string(sjv.nullable(), sjv.email())
   )),
   "price",           sjv.object(sjv.required(), sjv.fields(
     "value",         sjv.double(sjv.required()),
     "currency",      sjv.string(sjv.required(), sjv.max(3), sjv.filled())
   )),
   "packed",          sjv.boolean(sjv.required()),
   "home_currencies", sjv.array(sjv.required(), sjv.max(4), sjv.string(sjv.max(3))),
   "color",           sjv.string(sjv.nullable(), sjv.enum("red", "blue", "green", "yellow")),
   "active",          sjv.boolean()
)))
```

## Error messages in case of validation errors
As JSON is typically created by developers, and not end-users, the error messages returned by the SJV functionality are meant to help developers in solving issues with the JSON they provide. Here are some examples of error messages returned:
If the 'address' of the 'supplier' property does not have a 'street' property, then the [sjv.validate()](sjv.validate.md) function will set the following DAL error message: `"supplier.address.street is missing"`
If the 'currency' of the 'price' is an empty string, then the [sjv.validate()](sjv.validate.md) function will set the following DAL error message: `"price.currency must be filled; an empty string is not allowed"`
If 'color' property has the value "brown", then the [sjv.validate()](sjv.validate.md) function will set the following DAL error message: `"color is outside its valid range; only the following values are allowed: red, blue, green, yellow"`

## Creating reusable definitions
It is possible to create some reusable definitions, e.g., for supplier, address and price:
```

function extern string price.fields.def()
{
        |* defines price fields; this function can be used in object definitions, see below
        return(sjv.fields(
          "value",      sjv.double(sjv.required()),
          "currency",   sjv.string(sjv.required(), sjv.max(3), sjv.filled())
        ))
}

function extern string price.object.def()
{
        |* defines a price object
        return(sjv.object(sjv.required(), price.fields.def()))
}

function extern string address.fields.def()
{
        |* defines address fields; this function can be used in object definitions
        return(sjv.fields(
           "street",    sjv.string(sjv.required()),
           "number",    sjv.long(sjv.required()),
           "zip_code",  sjv.string(sjv.nullable(), sjv.alphanum())
        ))
}

function extern string address.object.def()
{
        |* defines an address object
        return(sjv.object(sjv.nullable(), address.fields.def()))
}

function extern string supplier.fields.def()
{
        |* defines supplier fields, reusing the address object definition
        return(sjv.fields(
           "name",         sjv.domain("tccom.bpid", sjv.required()),
           "address",      address.object.def(),
           "phone",        sjv.string(sjv.nullable()),
           "email",        sjv.string(sjv.nullable(), sjv.email())
        ))
}

function extern string supplier.object.def()
{
        |* defines a supplier object
        return(sjv.object(sjv.required(), supplier.fields.def()))
}
```
********

## Reusing definitions
These definitions can be reused as follows:
```

result = sjv.validate(json, sjv.object(sjv.required(), sjv.fields(
   "id",              sjv.string(sjv.required(), sjv.filled(), sjv.alphanum()),
   "name",            sjv.string(sjv.nullable(), sjv.filled()),
   "type",            sjv.string(sjv.required(), sjv.enum("product", "generic", "tool")),
   "supplier",        supplier.object.def(),
   "price",           price.object.def(),
   "packed",          sjv.boolean(sjv.required()),
   "home_currencies", sjv.array(sjv.required(), sjv.max(4), sjv.string(sjv.max(3))),
   "color",           sjv.string(sjv.nullable(), sjv.enum("red", "blue", "green", "yellow")),
   "active",          sjv.boolean()
)))
```
****

## Related topics
- [Simple JSON Validation overview](overview.md)
- [Simple JSON Validation synopsis](synopsis.md)
