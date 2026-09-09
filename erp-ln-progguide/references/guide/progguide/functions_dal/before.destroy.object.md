# before.destroy.object()

## Syntax:
`function function extern long before.destroy.object( )`

## Description
Use this to program checks that determine whether deleting a record is permitted.
*This object hook replaces the* before.delete subsection of the *main.table.io* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the necessary checks. Any *before.delete* sections in the UI script are ignored. So, if a UI script contains *before.delete* sections for the main table, you must replace these by *before.destroy.object()* hooks in the DAL.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Return value
The hook returns 0 if deleting the record is permitted. If the hook returns a negative value (DALHOOKERROR), the transaction is aborted.

## Example
```

function extern long before.destroy.object()
{
    if tdsls040.stat = tdsls.stat.invoiced then
        dal.set.error.message("tdsls44041")
        |* You cannot delete an invoiced transaction
        return(DALHOOKERROR)
    endif
    ...
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
