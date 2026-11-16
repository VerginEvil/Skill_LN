# dal.is.field.changed()

## Syntax:
`#include <bic_dam>`
`function boolean dal.is.field.changed( string fld.name, [ long element ] )`

## Description
Use this to test whether a field has changed. It is equivalent to:
`dal.get.field.mode(fld.name, [ element ] ) <> 0`

## Arguments
| | | |
|---|---|---|
| `string` | `fld.name` |  A string containing the field name  |
| `[ long` | `element ]` |  Optional element, use this in case of array elements  |

## Return values
TRUE in case the field has changed, FALSE in case the field has not changed.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function should not be used in the after.save.object section.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
