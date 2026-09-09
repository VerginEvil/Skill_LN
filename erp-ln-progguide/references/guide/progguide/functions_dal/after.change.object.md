# after.change.object()

## Syntax:
`function long after.change.object( )`

## Description
This hook is called after the current record has been changed, but not yet updated in the database. It marks the end of changing the current record.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook only applies to DAL2.
It is called by the [4GL engine](../glossary/glossary.md#fourgl_engine) at the moment the end-user presses the Save button for a modified record. It is also executed when a [dal.save.object()](../functions_db_operations/dal.save.object.md) is done. In both cases it is executed before any validations are performed.

## Return value
The hook normally returns 0. Do not return DALHOOKERROR to prevent the current record to be updated in the database. Only return DALHOOKERROR in case of unusual errors, like a data set-up problem.
Note  The main purpose of this hook to let the DAL know that the current record has been changed, but not yet updated in the database. It marks the end of the modification phase (setting field values).
It is not meant to prevent the current record to be updated in the database. Use the [method.is.allowed()](method.is.allowed.md) hook to prevent the current record to be updated in the database.

## Example
```

function extern long after.change.object()
{
    | The DAL now knows that the current record has been changed and that it
    | is about to be updated in the database.
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
