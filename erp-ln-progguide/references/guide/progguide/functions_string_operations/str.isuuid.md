# str.isuuid()

## Syntax:
`function boolean str.isuuid( const string string$ )`

## Description
Returns true if the given string is a valid UUID. A valid UUID has a length of 36 characters with 5 hexadecimal strings separated by the hyphen. The lengths of the parts are 8-4-4-4-12. Example: `550e8400-e29b-41d4-a716-446655440000`

## Arguments
| | | |
|---|---|---|
| `const string` | `string$` |  a string  |

## Return values
*true* if the string is a valid UUID, else *false*

## Context
This function is implemented in the 4GL Tools and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2495.

## Example
```

boolean	result

result = str.isuuid("550e8400-e29b-41d4-a716-446655440000")
|* result = true

result = str.isuuid("550e8400-a716-446655440000")
|* result = false

result = str.isuuid("550e8400-ABCD-41d4-a716-446655440000")
|* result = false
```

## Related topics
- [String operations overview](overview.md)
- [String operations synopsis](synopsis.md)
