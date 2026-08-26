# before.new.object()

## Syntax:
`function long before.new.object( )`

## Description
This hook is called when a new record is about to be created. It marks the start of creating a new record.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
This hook only applies to DAL2.
It is called by the 4GL engine at the moment the end-user presses the Insert button. It is also executed when a [dal.new.object()](../functions_db_operations/dal.new.object.md) or a [dal.copy.object()](../functions_db_operations/dal.copy.object.md) is done. In both cases it is executed before any defaults are set.

## Return value
The hook normally returns 0. Do not return DALHOOKERROR to prevent a new record to be created. Only return DALHOOKERROR in case of unusual errors, like a data set-up problem.
Note  The main purpose of this hook to let the DAL know that a new record is about to be created. It is not meant to prevent a new record to be created. Use the [method.is.allowed()](method.is.allowed.md) hook to prevent a new record to be inserted in the database.

## Example
```

function extern long before.new.object()
{
    | The DAL now knows that a new record is about to be created.
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [Object hooks](object_hooks.md)
