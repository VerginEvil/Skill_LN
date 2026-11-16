# before.change.object()

## Syntax:
`function long before.change.object( )`

## Description
This hook is called when the current record is about to be changed/modified. It marks the start of modifying the record.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook only applies to DAL2.
It is called by the [4GL engine](../glossary/glossary.md#fourgl_engine) at the moment the end-user starts modifying the record. It is also executed when a [dal.change.object()](../functions_db_operations/dal.change.object.md) is done.

## Return value
The hook normally returns 0. Do not return DALHOOKERROR to prevent the current record to be updated. Only return DALHOOKERROR in case of unusual errors, like a data set-up problem.
Note  The main purpose of this hook to let the DAL know that the current record is about to be changed. It is not meant to prevent the record to be updated in the database. Use the [method.is.allowed()](method.is.allowed.md) hook to prevent the record to be updated in the database.

## Example
```

function extern long before.change.object()
{
    | The DAL now knows that the current record is about to be changed.
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
