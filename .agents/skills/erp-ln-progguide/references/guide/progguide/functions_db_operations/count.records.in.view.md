# count.records.in.view()

## Syntax:
`function long count.records.in.view( )`

## Description
Counts the number of records that exist in the maintable for the current view. Any filter or query extension that has been set is taken into account.
This function can be used in combination with the [display.total.fields()](../functions_form_and_form_field_operations/display.total.fields.md) function.

## Return values
The number of records that are exists in the maintable for the current view.

## Context
This function is implemented in the 4GL Engine and can be used in 4GL script types.

## Example
```

function void update.total.line()
{
    long    rcd.count

    rcd.count = count.records.in.view()
    display.total.fields("fmfoc200.orno", rcd.count)
}
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
