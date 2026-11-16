# db.after.update()

## Syntax:
`function extern long db.after.update( )`

## Description
This hook is called in case data is updated, either by the user pressing the save button on the UI, or programmatically when one of the functions [dal.save.object()](../functions_db_operations/dal.save.object.md) or [dal.update()](../functions_db_operations/dal.update.md) is called.
Note that this hook is also executed in case a 'stand-alone'[db.update()](../functions_db_operations/db.update.md) is done.
This hook is executed just after the [db.update()](../functions_db_operations/db.update.md)
If this hook is called via a DAL function then the variable initiated.by.dal = true. If called via a DB function then this variable is false.

## Return values
This hooks returns 0 if deleting the record is permitted. It should return a negative value like DALHOOKERROR, in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.

## Example
```

function extern long db.after.update()
{
        | Do some extra actions just after the standard
        | update hook
        ...
        return(0)
}
```

## Related topics
- [DB DLL Overview](overview.md)

- [Data Access Layer](../functions_dal/overview.md)

- [Object hooks](../functions_dal/object_hooks.md)

- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
