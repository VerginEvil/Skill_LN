# JSON overview

## INTRODUCTION
JavaScript Object Notation (JSON) is a lightweight, text-based, language-independent data interchange format. It was derived from the ECMAScript Programming Language Standard. JSON defines a small set of formatting rules for the portable representation of structured data.
JSON is built on two structures:

- A collection of name/value pairs. In JSON this is called an object.

- An ordered list of values. In JSON this is called an array.

## OBJECT
An object is an unordered set of name/value pairs. An object begins with { (left brace) and ends with } (right brace). Each name is followed by: (colon) and the name/value pairs are separated by, (comma).

## ARRAY
An array is an ordered collection of values. An array begins with [ (left bracket) and ends with ] (right bracket). Values are separated by, (comma).

## VALUE
A value can be a string in double quotes, or a number, or true or false or null, or an object or an array. These structures can be nested.

## STRING
A string is a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes. A character is represented as a single character string. A string is very much like a C or Java string.

## NUMBER
A number is very much like a C or Java number, except that the octal and hexadecimal formats are not used.

## WHITESPACE HANDLING
Whitespace can be inserted between any pair of tokens.

## JSON API
The 3GL JSON API supports reading, writing, creating, manipulating and destroying JSON value instances. These instances can be of one of the following types:

- JSON_TYPE_NULL

- JSON_TYPE_BOOLEAN

- JSON_TYPE_NUMBER

- JSON_TYPE_OBJECT

- JSON_TYPE_ARRAY

- JSON_TYPE_STRING

The JSON API provides functions to test whether a value is a JSON value and to get the type of the JSON value instance.

## DEALING WITH JSON TYPES
Most JSON API functions accept a JSON value instance as the first parameter. It depends on the JSON type whether the function can deal with the passed JSON value. E.g. the Json.set() function can only deal with JSON values of type JSON_TYPE_OBJECT and the Json.add() function can only deal with JSON values of type JSON_TYPE_ARRAY.
In case a function cannot handle the passed JSON type, a runtime Assert message is given.

## DETACHING JSON INSTANCES
In order to prevent JSON structures from being corrupted, the JSON API is very strict regarding setting, adding, putting a JSON value in another JSON value, or deleting a JSON value. In case a JSON value is part of another JSON value, the operation is prevented and a runtime Assert message is given.
A JSON value must therefore be detached from its parent using Json.detach(), before such operations are done.

## ITERATING JSON STRUCTURES
For cases where the structure of the JSON value is not known, the JSON API provides functions for iterating a JSON structure.
Using an iterator is also the recommended way to traverse all values in a JSON array.

## READING AND WRITING JSON
The 3GL JSON API provides functions for reading JSON text from and writing JSON values to a string, a file or a stream.

## SUPPORTED ENCODINGS
Both UTF-8 and TSS encodings are supported for reading and writing JSON values.

## EXAMPLE USAGE
```

{
  "id": "ABC12345",
  "name": "ABC Bike",
  "supplier": {
    "name": "ACME_COMP",
    "address": {
      "street": "High Street",
      "number": 235,
      "zip code": "1234 AB"
    }
  },
  "price": 534.99,
  "packed": true,
  "currencies": [
    "EUR",
    "USD",
    "AUD"
  ],
  "color": null,
  "active": false
}
```
The JSON document above can be constructed as follows:
```

long	item
long	supplier
long	address
long	currencies

item = Json.newObject()
Json.setString(item, "id", "ABC12345")
Json.setString(item, "name", "ABC Bike")
supplier = Json.set(item, "supplier", Json.newObject())
Json.setString(supplier, "name", "ACME_COMP")
address = Json.set(supplier, "address", Json.newObject())
Json.setString(address, "street", "High Street")
Json.setNumber(address, "number", 235)
Json.setString(address, "zip code", "1234 AB")
Json.setNumber(item, "price", 534.99)
Json.setBoolean(item, "packed", true)
currencies = Json.set(item, "currencies", Json.newArray())
Json.add(currencies, "EUR")
Json.add(currencies, "USD")
Json.add(currencies, "AUD")
Json.setNull(item, "color")
Json.setBoolean(item, "active", false)
```
Retrieving data:
```

string	itemName(30)
string	zipCode(8)
string	currency(3)
string	color(12)
long	type

|* To get the item name
itemName = Json.getString(item, "name")

|* To get the value of the "zip code" field starting at the item level:
zipCode = Json.getString(Json.get(Json.get(item, "supplier"), "address"), "zip code")

|* The same, using the path
zipCode = Json.string(Json.path(item, "supplier", "address", "zip code"))

|* To get the 3rd currency:
currency = Json.stringAt(Json.get(item, "currencies"), 3)

|* The same, using the path
currency = Json.string(Json.path(item, "currencies", 3))

|* To get the value of color, which might be null
if not Json.isNull(Json.get(item, "color")) then
	color = Json.getString(item, "color"))
endif

|* To get the type of the price field
type = Json.type(Json.get(item, "price"))

if type = JSON_TYPE_NUMBER then
	|* ...
endif
```
Manipulating data:
```

|* To replace the 2nd currency with GBP
Json.putString(Json.get(item, "currencies"), 2, "GBP")

|* To delete the packed field
Json.del(item, "packed")

|* To delete the currencies array, it first needs to be detached from the item object
currencies = Json.get(item, "currencies")
Json.detach(currencies)
Json.delete(currencies)
```

## Related topics
- [JSON synopsis](synopsis.md)
