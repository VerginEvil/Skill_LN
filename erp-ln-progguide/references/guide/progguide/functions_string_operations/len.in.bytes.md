# len.in.bytes()

## Syntax:
`function long len.in.bytes( string value )`

## Description
This function returns the [length in bytes (byte length)](../3gl_features/data_types.md#byte length) of the supplied string argument.
Notice that for single-byte strings there is *no* difference between the [byte length](../3gl_features/data_types.md#byte length) and the [character length](../3gl_features/data_types.md#character length). Consequently, for single-byte strings there is *no* difference between the bshell functions `len.in.bytes()` and [len()](len.md).

## Arguments
| | | |
|---|---|---|
| `string` | `value` |    |

## Return values
This function returns the [length in bytes (byte length)](../3gl_features/data_types.md#byte length) of the supplied string argument. Notice that, regarding the byte length, there is no difference between a single-byte string value and a [multibyte string value](../3gl_features/multibyte_strings.md#byte length).

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long      lng
string    var(20)
string    fix(20)    fixed

var = "abc"
fix = "abc"

lng = len.in.bytes( var )             | Returns 3
lng = len.in.bytes( fix )             | Returns 20
lng = len.in.bytes( strip$(fix) )     | Returns 3
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
