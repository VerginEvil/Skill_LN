# argc()

## Syntax:
`function long argc( )`

## Description
This returns the number of arguments of the current program. You can pass arguments to the program by activating it with the [activate()](activate.md), [act.and.sleep()](act.and.sleep.md), or [wait.and.activate()](wait.and.activate.md) functions.

## Context
This function is implemented in the porting set and can be used in all script types.

## Example
```

string    str_arr(10, 4)           | 4 strings of length 10
activate("other_program", str_arr) | argc() in other_program has
the value 5
```

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
