# refresh.total.line()

## Syntax:
`function void refresh.total.line( )`

## Description
This triggers the 4GL-Engine to execute the program section: [on.display.total.line](../4gl_features/4gl_program_sections.md). This section is not called directly but after all other sections have been executed. This function can be useful when the total line must be updated immediately after a user action or a change of a field value. When this function is not used, the program section *on.display.total.line* is only called after reading a new set of records from the database.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  This function is available from [TIV](../tiv/tiv_overview.md) [TIV 1075](../tiv/tiv_1075.md).

## Example
```

field.tewhr004.weight:
when.field.changes:
    refresh.total.line()
```

## Related topics
- [Form and form field operations overview](overview.md)

- [Form and form field operations synopsis](synopsis.md)
