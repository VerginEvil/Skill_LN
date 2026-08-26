# btol()

## Syntax:
`function long btol( boolean boolean_value )`

## Description
Cast a boolean to a long.

## Arguments
| | | |
|---|---|---|
| `boolean` | `boolean_value` |  boolean to cast to a long.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

boolean boolean_var
long long_var

boolean_var = true
long_var = btol( boolean_var )    | long_var contains 1
```
