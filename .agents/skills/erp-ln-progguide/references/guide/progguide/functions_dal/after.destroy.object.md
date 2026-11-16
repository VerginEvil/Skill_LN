# after.destroy.object()

## Syntax:
`function long after.destroy.object( )`

## Description
Use this to update referenced tables after the current object has been deleted.
*This object hook replaces the* after.delete subsection of the *main.table.io* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the necessary actions. Any *after.delete* sections in the UI script are ignored. So, if a UI script contains *after.delete* sections for the main table, you must replace these by *after.destroy.object()* hooks in the DAL.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Return value
The hook returns 0 if successful. If the hook returns a negative value (DALHOOKERROR), the transaction is aborted.

## Example
```

function extern long after.destroy.object()
{
    return(0)
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
