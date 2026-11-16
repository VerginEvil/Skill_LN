# do.occ()

## Syntax:
`function void do.occ( long occurrence, <function_name>, [ <type>... ] )`

## Description
This locks the specified occurrence (delayed lock) and executes the specified function for that occurrence. After the function has been executed all fields of the specified occurrence are redisplayed.

## Arguments
| | | |
|---|---|---|
| `long` | `occurrence` |  The occurrence number.  |
| `<function_name>` |  | The name of the function that must be executed. The function must be of type void. |
| `[ <type>` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function. Use commas (,) to separate the arguments.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## See also
[do.all.occ()](do.all.occ.md), [do.occ.without.update()](do.occ.without.update.md), [do.selection()](do.selection.md), [on.old.occ()](on.old.occ.md)

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
