# ue.after.after.save.object()

## Syntax:
`function extern long ue.after.after.save.object( [ long mode ] )`

## Description
This hook is called in case data is saved, either by the user pressing the save button on the UI, or programmatically when one of the functions [dal.save.object()](../functions_db_operations/dal.save.object.md), [dal.new()](../functions_db_operations/dal.new.md), or [dal.update()](../functions_db_operations/dal.update.md) is called.
Note that this hook is also executed in case a 'stand-alone'[db.insert()](../functions_db_operations/db.insert.md) or a [db.update()](../functions_db_operations/db.update.md) is done.
In case a DAL is present, this hook is executed just after the [after.save.object()](../functions_dal/after.save.object.md) hook.
In case no DAL is present, this hook is executed just after the `main.table.io:after.write:` and `main.table.io:after.rewrite:` UI script sections.
In case of a 'stand-alone'[db.update()](../functions_db_operations/db.update.md) or [db.insert()](../functions_db_operations/db.insert.md), this hook is executed after the database operation itself and just after the [ue.before.after.save.object()](ue.before.after.save.object.md) hook.

## Arguments
| | | |
|---|---|---|
| `[ long` | `mode ]` |  This parameter contains either the value DAL_NEW in case of an insert, or DAL_UPDATE in case of an update.  |

## Return values
This hooks returns 0 if saving the record is permitted. It should return a negative value like DALHOOKERROR, in case of an error.

## Context
This function is implemented in the 4GL Engine and can be used in UEDLL script types.

## Example
```

function extern long ue.after.after.save.object(long mode)
{
        on case mode
        case DAL_NEW:
                break
        case DAL_UPDATE:
                | Do some extra actions just after the standard
                | after.save.object hook
                ...
                break
        endcase

        return(0)
}
```

## Related topics
- [User Exit DLL Overview](overview.md)

- [Data Access Layer](../functions_dal/overview.md)

- [Object hooks](../functions_dal/object_hooks.md)

- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
