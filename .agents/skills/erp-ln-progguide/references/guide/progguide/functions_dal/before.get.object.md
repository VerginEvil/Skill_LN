# before.get.object()

## Syntax:
`function function extern long before.get.object( long direction )`

## Description
Use this to program checks that determine whether reading a record is permitted. The argument is set by the STP or CDAS and specifies the object being read. The possible values are:
DAL_GET_FIRST DAL_GET_NEXT DAL_GET_PREV
DAL_GET_LAST DAL_FIND DAL_GET_CURR
This object hook replaces the *before.read* subsection of the *main.table.io* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the necessary checks. Any *before.read* sections in the UI script are ignored. So, if a UI script contains *before.read* sections for the main table, you must replace these by *before.get.object()* hooks in the DAL.

## Arguments
| | | |
|---|---|---|
| `long` | `direction` |    |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Return value
The hook returns 0 if reading of the record is permitted. Negative return values (DALHOOKERROR) are ignored by the calling program.
Note  This hook is only executed in case the [4GL engine](../glossary/glossary.md#fourgl_engine) reads data from the maintable. It is *not* executed when you do [dal.new()](../functions_db_operations/dal.new.md), [dal.update()](../functions_db_operations/dal.update.md) or [dal.destroy()](../functions_db_operations/dal.destroy.md).

## Example
```

function extern long before.get.object(long dir)
{
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
