# dal.parent.caused.update()

## Syntax:
`#include <bic_dal>`
`function boolean dal.parent.caused.update( string fld.name, [ long element ] )`

## Description
This function may only be called within an `.update()` hook. It checks whether this call to this hook was triggered by a change in field *fld.name*.

## Arguments
| | | |
|---|---|---|
| `string` | `fld.name` |  A string containing the name of the field (e.g., "whinh312.lsta"). The current field must depend directly on *fld.name* for HOOK_UPDATE.  |
| `[ long` | `element ]` |  optional element of the field in case of array fields (default is 1)  |

## Return values
true or false

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
