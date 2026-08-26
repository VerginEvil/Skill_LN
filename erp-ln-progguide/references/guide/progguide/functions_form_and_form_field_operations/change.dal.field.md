# change.dal.field()

## Syntax:
`function void change.dal.field( string field, void value )`

## Description
Changes the value of the given table field and calls the DAL Layer to update any dependent fields. Afterwards, the UI is updated.

## Arguments
| | | |
|---|---|---|
| `string` | `field` |  The name of the field to change, in the format "fieldname" or "fieldname(element)"  |
| `void` | `value` |  the value to assign to the field  |

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.
Note  The given field must be a field of the maintable
Can be called in the when.field.changes, before.new.object and after.zoom sections.

## Example
```

|* Changing a non array field
change.dal.field("tfgld102.leac", ledger.account)

|* Changing an array field
change.dal.field("tfgld102.amth(1)", home.amount(1))
change.dal.field("tfgld102.amth(2)", home.amount(2))
change.dal.field("tfgld102.amth(3)", home.amount(3))

|* Changing a string array field
change.dal.field("tcfin110.dimx(1)", dimensions(1,1))
change.dal.field("tcfin110.dimx(2)", dimensions(1,2))
change.dal.field("tcfin110.dimx(3)", dimensions(1,3))
change.dal.field("tcfin110.dimx(4)", dimensions(1,4))

|* Or using a "for" loop instead:
for i = 1 to 4
    change.dal.field("tcfin110.dimx(" & str$(i) & ")", dimensions(1,i))
endfor
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
