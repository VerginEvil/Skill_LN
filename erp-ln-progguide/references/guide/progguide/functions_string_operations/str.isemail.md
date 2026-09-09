# str.isemail()

## Syntax:
`function boolean str.isemail( const string string$ )`

## Description
Returns true if the given string contains an email address. This function defines any string to be an email address if it has the following format:
```
<local-part>@<domain-part>
```
where:

- `<local-part>` is not empty

- `<domain-part>` is not empty, contains at least one dot, does not start with a dot and does not end with a dot

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string contains a valid email address, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isemail("info@example.com")
|* result = true

result = str.isemail("info@example")
|* result = false

result = str.isemail("@example.com")
|* result = false
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
