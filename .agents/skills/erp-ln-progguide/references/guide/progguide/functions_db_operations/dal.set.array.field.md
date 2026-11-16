# dal.set.array.field()

## Syntax:
`#include <bic_dam>`
`function void dal.set.array.field( string fld.name, void value )`

## Description
Sets the value of the given array field and informs the DAL that the field is changed. This function assigns a complete array at once. If you want to set only one or a few array elements, use function [dal.set.field()](dal.set.field.md).
The number of elements to set will be equal to the minimum of the array depth and the field depth. Example:

- If the array depth is 2 and the field depth is 3, only the first 2 elements of the field will be assigned a value;

- If the array depth is 4 and the field depth is 3, the last element of the array will not be used.

This function is a shorthand for the following (pseudo) code:
```

        long   i
        long   depth

        depth = <the minimum value of the field depth and the array depth>
        if <array type is STRING> then
                for i = 1 to depth
                        dal.set.field(fld.name, value(1,i), i)
                endfor
        else
                | Type is LONG or DOUBLE
                for i = 1 to depth
                        dal.set.field(fld.name, value(i), i)
                endfor
        endif
```

## Arguments
| | | |
|---|---|---|
| `string` | `fld.name` |  the name of the array field  |
| `void` | `value` |  an array containing the new values for the field  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1900.

## Preconditions
- When used in a DAL hook, other than the [set.object.defaults()](../functions_dal/set.object.defaults.md) hook, it is only possible to set fields of other DALs. See [dal.set.field()](dal.set.field.md) for more information.

- Argument *fld.name* must be the name of an existing, valid array field

- Argument *value* must be an array and memory must have been allocated. So passing a based array for which no alloc.mem() has been done yet, is not allowed.

Note  This function does not update any dependent fields itself, nor does it check the field's value! These actions are done during a save.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)

- [dal.set.field()](dal.set.field.md)
