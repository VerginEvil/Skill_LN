# activate.search()

## Syntax:
`function void activate.search( )`

## Description
This forces a random search action on the main table. You call the function immediately after input to a field during insertion of a new record (standard command ADD.SET or DUPL.OCCUR) or during MODIFY.SET (if the predefined variable *modify.prim.key* is set to TRUE).
When a new record is being added to the database, the [4GL engine](../glossary/glossary.md#fourgl_engine) normally executes a search action in the main table after input to the field(s) of the primary index. If the key values entered belong to an existing record in the main table, the [4GL engine](../glossary/glossary.md#fourgl_engine) displays all the fields of that record and stops adding the new record. Otherwise, the user must fill the remaining fields; then the record is added to the main table.
In some applications, not all parts of the primary index appear on the form. In this case, the search operation in the main table occurs when the user leaves the last input field of the occurrence. You can force an earlier search action by calling *activate.search()* after input to any field of the occurrence.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

| Suppose there are 2 input fields on the form, 'number' and
| 'name', which are not parts of the primary index of the main
| table. When the user leaves the field 'number', a search action in
| the main table should be done by the 4GL engine:
field.number:
on.input:
                activate.search()
```

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
