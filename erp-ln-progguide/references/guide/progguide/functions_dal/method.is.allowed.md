# method.is.allowed()

## Syntax:
`function boolean method.is.allowed( long method )`

## Description
This is a special hook for handling centralized authorizations. Use it to perform checks that determine whether certain Data Access Methods are permitted for an object. The *method* argument specifies the method to check.

## Arguments
| | | |
|---|---|---|
| `long` | `method` |    |

## Return values
TRUE if the method is permitted
FALSE if the method is not permitted

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## When called
The hook can be called from the UI script, but it is also called from the [4GL engine](../glossary/glossary.md#fourgl_engine) to check whether certain operations are allowed.
For [Extended DAL (DAL2)](dal2_overview.md), the [4GL engine](../glossary/glossary.md#fourgl_engine) will call this hook also to determine whether the standard commands ADD.SET, DUPL.OCCUR, MODIFY.SET and MARK.DELETE have to be disabled. This is done just before calling the following UI script sections:

- *before.display.object*

- *when.field.changes*

- *read.view* subevent of the *main.table.io*

- *after.choice* subevent of the *choice.mark.occur*

This hook is also called by the [dal.save.object()](../functions_db_operations/dal.save.object.md) and [dal.destroy.object()](../functions_db_operations/dal.destroy.object.md) functions.

## The DAL_NEW method
When this hook is called for the DAL_UPDATE and DAL_DESTROY methods, then you can check current record values to determine whether these methods are permitted. However, when this hook is called for the DAL_NEW method then you should *not* check current record values, but e.g. parameter settings or data from other tables, or a parent record. The reason is that a record itself cannot tell whether records may be added to the table.
It is however, perfectly allowed to check for a parent record, no matter whether this parent record exists in another table or the same table. An example would be to use the method.is.allowed hook of a Order Lines table that asks its related Header whether new Order Lines may be inserted.
Another example would be a hierarchy (like an Item BOM). A child in the tree can ask its parent, to see whether that parent allows more children being added to that parent.

## Example
```

function extern boolean method.is.allowed(long method)
{
    on case method
    case DAL_NEW:
        if .... then
            dal.set.error.message("error message")
            return(false)
        endif
    break
    case DAL_UPDATE:
        ...
        break
    case DAL_DESTROY:
        ...
        break
    endcase
    return(true)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
