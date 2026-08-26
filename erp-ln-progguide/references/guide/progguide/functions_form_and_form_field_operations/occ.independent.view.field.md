# occ.independent.view.field()

## Syntax:
`function void occ.independent.view.field( string field.name )`

## Description
This defines the specified field as occurrence independent. This means that its value is not stored in one of the records that is shown in the grid. An example is an order total field that is shown in the grid. Another example is a field that is used to filter out records.
Occurrence independent fields are treated in a special way. When normal fields get input, the update.status and choice variables will be set (if they do not already have a value) and the record will be locked (delayed lock). This is not the case for occurrence independent fields, which makes them perfectly suitable for e.g. filtering functionality.

## Arguments
| | | |
|---|---|---|
| `string` | `field.name` |  The name of the field that must be defined as occurrence independent.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  It is preferred to define a field as occurrence independent in the DFE (Dynamic Form Editor). See the Position tab of the Field Properties dialog in the DFE. Only in case a field is defined as occurrence independent under certain conditions you should use this function.

## Example
```

after.form.read:
    if <parameter has a certain value> then
        occ.independent.view.field("total.hours")
    endif
```

## Related topics
- [Form and form field operations overview](overview.md)
- [Form and form field operations synopsis](synopsis.md)
