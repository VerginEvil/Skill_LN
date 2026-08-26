# do.occ.without.update()

## Syntax:
`function long do.occ.without.update( long occurrence, function_name function_name, function_name ... )`

## Description
This executes the specified function for a specified occurrence, without any locking or update actions. After the function has been executed all fields of the specified occurrence are redisplayed.

## Arguments
| | | |
|---|---|---|
| `long` | `occurrence` |  The occurrence number.  |
| `function_name` | `function_name` |  The name of the function that must be executed. The function must be of type void.  |
| `function_name` | `...` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[do.all.occ()](do.all.occ.md), [do.occ()](do.occ.md), [do.selection()](do.selection.md), [on.old.occ()](on.old.occ.md)

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
