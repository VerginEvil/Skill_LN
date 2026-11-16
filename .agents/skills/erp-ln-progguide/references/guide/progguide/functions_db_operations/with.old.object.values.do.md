# with.old.object.values.do()

## Syntax:
`#include <bic_dal>`
`function void with.old.object.values.do( <function_name>, [ <type>... ] )`

## Description
This executes the specified function for the current record, using the old values of the record. The record must have been previously modified.
You can call this function in the field hooks and the [before.save.object()](../functions_dal/before.save.object.md) hook of a DAL script. It is the equivalent of the [on.old.occ()](../functions_form_and_form_field_operations/on.old.occ.md) function used in UI scripts.

## Arguments
| | | |
|---|---|---|
| `<function_name>` |  | The name of the function that must be executed. The function must be of type void. |
| `[ <type>` | `... ]` |  Use these optional arguments to pass one or more arguments to the specified function.  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.
Note  It is not supported to use this function in a nested way.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
