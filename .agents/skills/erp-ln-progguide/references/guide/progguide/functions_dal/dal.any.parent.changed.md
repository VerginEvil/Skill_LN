# dal.any.parent.changed()

## Syntax:
`#include <bic_dal>`
`function boolean dal.any.parent.changed( )`

## Description
The function dal.any.parent.changed() determines whether any of the fields, from which the current field depends, is changed. This function can only be used in combination with [dal.require.field()](dal.require.field.md).

## Return values
true one or more parent fields have changed
false no parent field has changed

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types. This function is available from [TIV](../tiv/tiv_overview.md) level 1300.
Note  This function can only be called in the [field.update()](field.update.md) hook.
