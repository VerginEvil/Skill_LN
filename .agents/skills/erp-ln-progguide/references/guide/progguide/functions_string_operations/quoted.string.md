# quoted.string()

## Syntax:
`function string quoted.string( string expr )`

## Description
*quoted.string()* assures that the contents of the variable can be used as a string for the query processor. If the string_expr contains a quote or double quote, the query processor will generate an error. This function inserts the necessary escapes for the string.

## Arguments
| | | |
|---|---|---|
| `string` | `expr` |    |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  These functions can handle multibyte characters.

## Example
```

query.extend.where("tcibd001.item <> """ & tibom010.mitm & """")      | WRONG
query.extend.where("tcibd001.item <> " & quoted.string(tibom010.mitm))        | CORRECT
```

## Related topics
- [String operations overview](overview.md)

- [String operations synopsis](synopsis.md)
