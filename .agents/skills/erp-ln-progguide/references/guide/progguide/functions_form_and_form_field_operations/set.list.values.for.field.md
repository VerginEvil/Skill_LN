# set.list.values.for.field()

## Syntax:
`function void set.list.values.for.field( const string field.name.string, long no.list.values, const string list.values(,) )`

## Description
This fills a listbox field or a combobox field with a specified set of values. The field must be a string type field, and the appearance must be set to Dropdown Listbox or Dropdown Combobox in the DFE.

## Arguments
| | | |
|---|---|---|
| `const string` | `field.name.string` |  The name of the string field. For example, "prog.code". For an array field, include the array element. For example, "prog.code(5)".  |
| `long` | `no.list.values` |  Number of values present in the list.values array  |
| `const string` | `list.values(,)` |  A string array that contains all values that need to be placed in the listbox field. It should contain the number of entries as indicated by the no.list.values argument.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function cannot be used in the before.program or after.form.read section, and cannot be used on fields in a grid.

## Example
```

declaration:
    extern  domain  ttadv.cpac  package | Form field

group.1:
init.group:
        long    i
        string  list.values(1, 1)       based

        i = 0
        select  cpac
    from    ttadv100
    selectdo
        if certain_condition() then
            i = i + 1
            alloc.mem(list.values, 30, i)
            list.values(1, i) = ttadv100.cpac
        endif
    endselect

    set.list.values.for.field("package", i, list.values)
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
