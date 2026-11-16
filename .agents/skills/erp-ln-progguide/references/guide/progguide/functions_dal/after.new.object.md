# after.new.object()

## Syntax:
`function long after.new.object( )`

## Description
This hook is called after a new record has been created, but not yet saved in the database. It marks the end of creating a new record.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook only applies to DAL2.
It is called by the [4GL engine](../glossary/glossary.md#fourgl_engine) at the moment the end-user presses the Save button for a new record. It is also executed when a [dal.save.object()](../functions_db_operations/dal.save.object.md) is done. In both cases it is executed before any validations are performed.

## Return value
The hook normally returns 0. Do not return DALHOOKERROR to prevent a new record to be created. Only return DALHOOKERROR in case of unusual errors, like a data set-up problem.
Note  The main purpose of this hook to let the DAL know that a new record has been created, but not yet saved in the database. It marks the end of the creation phase (setting field values).
It is not meant to prevent a new record to be created. Use the [method.is.allowed()](method.is.allowed.md) hook to prevent a new record to be inserted in the database.

## Example
```

function extern long after.new.object()
{
    | The DAL now knows that a new record has been created and that it
    | is about to be inserted in the database.
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
