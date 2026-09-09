# db.before.insert()

## Syntax:
`function extern long db.before.insert( )`

## Description
This hook is called in case data is inserted, either by the user pressing the save button on the UI, or programmatically when one of the functions [dal.new.object()](../functions_db_operations/dal.new.object.md) or [dal.new()](../functions_db_operations/dal.new.md) is called.
Note that this hook is also executed in case a 'stand-alone'[db.insert()](../functions_db_operations/db.insert.md) is done.
This hook is executed before the [db.insert()](../functions_db_operations/db.insert.md) operation.
If this hook is called via a DAL function then the variable initiated.by.dal = true. If called via a DB function then this variable is false.

## Return values
This hooks returns 0 if deleting the record is permitted. It should return a negative value like DALHOOKERROR, in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in 3GL script types.

## Example
```

function extern long db.before.insert()
{
        | Do some extra actions just before the standard
        | db.insert
        ...
        return(0)
}
```

## Related topics
- [DB DLL Overview](overview.md)

- [Data Access Layer](../functions_dal/overview.md)

- [Object hooks](../functions_dal/object_hooks.md)

- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
