# after.get.object()

## Syntax:
`function extern long after.get.object( long direction )`

## Description
Use this, to program checks that determine whether reading a record is permitted. The checks are performed after the record has been retrieved from the database. The *dir* argument is set by the STP and specifies the object being read. The possible values are:
DAL_GET_FIRST DAL_GET_NEXT DAL_GET_PREV
DAL_GET_LAST DAL_FIND DAL_GET_CURR
*This object hook replaces the* after.read subsection of the *main.table.io* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the necessary checks. Any *after.read* sections in the UI script are ignored. So, if a UI script contains *after.read* sections for the main table, you must replace these by *after.get.object()* hooks in the DAL.

## Arguments
| | | |
|---|---|---|
| `long` | `direction` |  |

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Return value
The hook returns 0 if reading of the record is permitted. If the hook returns a negative value (DALHOOKERROR), the object is skipped.
Notes  This hook is only executed in case the 4GL engine reads data from the maintable. It is *not* executed when you do [dal.new()](../functions_db_operations/dal.new.md), [dal.update()](../functions_db_operations/dal.update.md) or [dal.destroy()](../functions_db_operations/dal.destroy.md).
It is preferable to use a [Query extensions](query_extensions.md) in the *before.program* section of the UI script instead of this hook. So, only use this hook if a query extension is not possible.
The 4GL engine ignores messages set in this hook.

## Example
```

| after.get.object hook

function extern long after.get.object(long dir)
{
    on case dir
    case DAL_GET_FIRST:
        …
        break
    case DAL_GET_NEXT:
        …
        break
    case DAL_GET_PREV:
        …
        break
    case DAL_GET_LAST:
        …
        break
    case DAL_FIND:
        …
        break
    case DAL_GET_CURR:
        …
        break
    default:
        …
        break
    endcase
    if ttadv100.cpac = "tt"
        return(DALHOOKERROR)
        | Error messages from after.get.object are
        | ignored by the 4GL engine
    endif
    return(0)
}

| Query extension with the same result
| Use this in preference
before.program:
    query.extend.where("ttadv100.cpac <> ""tt"" ")
```

## Related topics
- [Data Access Layer](overview.md)
- [DAL terminology](dal_glossary.md)
- [Object hooks](object_hooks.md)
