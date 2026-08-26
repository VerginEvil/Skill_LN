# dal.save.object()

## Syntax:
`#include <bic_dam>`
`function long dal.save.object( string tbl.name, [ long error.flag ] )`

## Description
Saves a record of the given table. In case a [dal.new.object()](dal.new.object.md) or a [dal.copy.object()](dal.copy.object.md) was done, the record is inserted in the database. In case a [dal.change.object()](dal.change.object.md) was done, the record is updated in the database.
In case [DAL2 Field dependencies](../functions_dal/dal2_field_dependencies.md) have been defined in the DAL, this function takes care that dependent fields will be triggered in the right order so that they can update themselves.
Note that this is done based on the values of the fields that have been set by calling [dal.set.field()](dal.set.field.md)
Before the record is saved all (changed) fields will be validated.
The sequence of the actions is as follows:
1. Table level permission is checked.
1. For all fields set, the [fieldname.make.valid()](../functions_dal/fieldname.make.valid.md) is executed, e.g. to perform rounding of data.
1. All dependent fields are triggered to update themselves.
1. Record level permission is checked.
1. The actual save (insert or update) is done.

## Arguments
| | | |
|---|---|---|
| `string` | `tbl.name` |  the table name of the DAL.  |
| `[ long` | `error.flag ]` |  For some errors, it is possible to indicate the action the system must perform when the error occurs. You use this argument to specify the required action(s). See [Error handling](../functions_database_handling/error_handling.md)  |

## Return values
| | |
|---|---|
| 0 | Record is saved |
| DALHOOKERROR | One of the hooks blocked the save action |
| DALDBERROR | A domain or reference error occurred (only in Integration context (e.g. via a BOL))  |
| DALNOSETPERM | No table level permission |
| DALNOOBJPERM | No record level permission |
| > 0 | The error code of the db.insert() or db.update() function  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Hooks called
- [before.open.object.set()](../functions_dal/before.open.object.set.md) if this is the first call to the DAL
- [after.new.object()](../functions_dal/after.new.object.md) in case of a new record
- [after.change.object()](../functions_dal/after.change.object.md) in case of an existing record
- for all fields set, the [fieldname.make.valid()](../functions_dal/fieldname.make.valid.md) hook is executed
- for each dependent field:
-
- [field.update()](../functions_dal/field.update.md)
- [method.is.allowed()](../functions_dal/method.is.allowed.md)
- for each (DAL_NEW) / each changed (DAL_UPDATE) field:
-
- one or more field hooks
- [before.save.object()](../functions_dal/before.save.object.md)
- [after.save.object()](../functions_dal/after.save.object.md)

## Error Handling
In case a database error occurs (a return value greater than 0), then this function will set an error message. E.g. in case a record is modified by another user then an error message is set.
Note  When working with DAL2 DALs, it is advised to use dal.save.object() instead of [dal.new()](dal.new.md) or [dal.update()](dal.update.md). Only then field dependencies are taken into account.
In case the DAL does not have field dependencies defined, or if you don't want to set defaults based on field dependencies, you can also use [dal.new()](dal.new.md) or [dal.update()](dal.update.md). These functions are faster than dal.save.object().

## Example
```

function extern long temmt020.insert(
        domain  tegen.code  currency,
        domain  tegen.code  category,
        domain  tegen.symb  symbol,
        domain  tegen.code  sub.code,
        domain  tegen.symb  sub.symbol,
        domain  tegen.isoc  iso.code,
        domain  tegen.ison  iso.number)
{
    FunctionUsage
    Inserts a currency. Only the required fields have to be
specified.
    This function accepts 7 parameters. Based on these the other
table fields
    will get correct default values.
    ...
    EndFunctionUsage

    long    result

    |* Start insert, sets object defaults
    result = dal.new.object("temmt020")
    ...

    |* Set fields
    dal.set.field("temmt020.curr", currency)
    dal.set.field("temmt020.catg", category)
    dal.set.field("temmt020.symb", symbol)
    dal.set.field("temmt020.subc", sub.code)
    dal.set.field("temmt020.subs", sub.symbol)
    dal.set.field("temmt020.isoa", iso.code)
    dal.set.field("temmt020.isob", iso.number)

    |* Save the record. This will make sure that all fields will
    |* get a correct value, based on the field dependencies defined for this DAL.
    result = dal.save.object("temmt020")
    ...

    return(result)
}
```

## Related topics
- [Database operations overview](overview.md)
- [Database operations synopsis](synopsis.md)
