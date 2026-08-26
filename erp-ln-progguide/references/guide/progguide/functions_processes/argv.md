# argv$()

## Syntax:
`function string argv$( long num_expr )`

## Description
This returns the specified argument of the program as a string. The program name is stored in ARGV$(0). The last argument is stored in ARGV$( ARGC()-1 ).
You can pass arguments to the program by activating it with the [activate()](activate.md), [act.and.sleep()](act.and.sleep.md), or [wait.and.activate()](wait.and.activate.md) functions. When you pass a string array as an argument, all elements of the array are passed as single arguments.

## Arguments
| | | |
|---|---|---|
| `long` | `num_expr` |  |

## Return values
The specified argument as a string. Or an empty string (“”) if the argument does not exist.

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Processes overview and synopsis](overview_and_synopsis.md)
