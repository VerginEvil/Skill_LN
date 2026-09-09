# with.object.set.do()

## Syntax:
`#include <bic_dal>`
`function void with.object.set.do( <function_name>, [ <type>... ] )`

## Description
With this function you can perform actions on records in the DAL's table, without affecting the current record. First the current record is saved into a temporary record buffer, then the specified function is executed. Afterwards the current record is restored from the temporary buffer.
You can call this function in any DAL hook. It is the equivalent of the [on.main.table()](on.main.table.md) function used in UI scripts.

## Arguments
| | | |
|---|---|---|
| `<function_name>` |  | The name of the function that must be executed. The function must be of type void. |
| `[ <type>` | `... ]` |  Use these optional arguments to pass one or more arguments to the function.  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL and DB DLL script types.
Note  It is not supported to use this function in a nested way.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
