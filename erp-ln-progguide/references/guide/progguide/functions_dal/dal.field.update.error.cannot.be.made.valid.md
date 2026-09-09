# dal.field.update.error.cannot.be.made.valid()

## Syntax:
`function void dal.field.update.error.cannot.be.made.valid( )`

## Description
Use this function when an error from field.update may not be changed or corrected by the [fieldname.make.valid()](fieldname.make.valid.md) hook, but it must always result in an error.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2521.
Note  This function is only allowed in the [field.update()](field.update.md) hook.

## Related topics
- [Extended DAL (DAL2)](dal2_overview.md)

- [DAL2 Field dependencies](dal2_field_dependencies.md)

- [DAL2 and the 4GL Engine](dal2_4gle.md)

- [DAL2 Flow of field hooks](dal2_flow.md)
