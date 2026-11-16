# ltob()

## Syntax:
`function boolean ltob( long long_value )`

## Description
Cast a long to a boolean.

## Arguments
| | | |
|---|---|---|
| `long` | `long_value` |  long to cast to a boolean.  |

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

long long_var
boolean boolean_var

long_var = 2
boolean_var = ltob( long_var )    | boolean_var contains true
```
