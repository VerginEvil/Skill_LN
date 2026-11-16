# len()

## Syntax:
`function long len( string value )`

## Description
This function returns the [length in characters (character length)](../3gl_features/data_types.md#character length) of the supplied string argument.
Notice that for single-byte strings there is *no* difference between the [byte length](../3gl_features/data_types.md#byte length) and the [character length](../3gl_features/data_types.md#character length). Consequently, for single-byte strings there is *no* difference between the bshell functions `len()` and [len.in.bytes()](len.in.bytes.md).

## Arguments
| | | |
|---|---|---|
| `string` | `value` |    |

## Return values
This function returns the [length in characters (character length)](../3gl_features/data_types.md#character length) of the supplied string argument. Notice that, regarding the character length, there is a difference between a single-byte string value and a [multibyte string value](../3gl_features/multibyte_strings.md#character length).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long      lng
string    var(20)
string    fix(20)    fixed

var = "abc"
fix = "abc"

lng = len( var )             | Returns 3
lng = len( fix )             | Returns 20
lng = len( strip$(fix) )     | Returns 3
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
