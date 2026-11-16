# ue.after.after.destroy.object()

## Syntax:
`function extern long ue.after.after.destroy.object( )`

## Description
This hook is called in case data is deleted, either by the user pressing the delete button on the UI, or programmatically when one of the functions [dal.destroy.object()](../functions_db_operations/dal.destroy.object.md) or [dal.destroy()](../functions_db_operations/dal.destroy.md) is called.
Note that this hook is also executed in case a 'stand-alone'[db.delete()](../functions_db_operations/db.delete.md) is done.
In case a DAL is present, this hook is executed just after the [after.destroy.object()](../functions_dal/after.destroy.object.md) hook.
In case no DAL is present, this hook is executed just after the `main.table.io:after.delete:` UI script section.
In case of a 'stand-alone'[db.delete()](../functions_db_operations/db.delete.md) this hook is executed after the db.delete() operation and just after the [ue.before.after.destroy.object()](ue.before.after.destroy.object.md) hook.

## Return values
This hooks returns 0 if deleting the record is permitted. It should return a negative value like DALHOOKERROR, in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in UEDLL script types.

## Example
```

function extern long ue.after.after.destroy.object()
{
        | Do some extra actions just after the standard
        | after.destroy.object hook
        ...
        return(0)
}
```

## Related topics
- [User Exit DLL Overview](overview.md)

- [Data Access Layer](../functions_dal/overview.md)

- [Object hooks](../functions_dal/object_hooks.md)

- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
