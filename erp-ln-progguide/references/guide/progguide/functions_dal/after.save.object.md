# after.save.object()

## Syntax:
`function long after.save.object( long mode )`

## Description
Use this to update referenced tables after a record has been added or updated. The *mode* argument is set by the [4GL engine](../glossary/glossary.md#fourgl_engine). The possible values are:
DAL_NEW indicates a new record
DAL_UPDATE indicates a record being updated
*This object hook replaces the* after.write and *after.rewrite* subsections of the *main.table.io* event section in a UI script. If there is a DAL for an object set, this hook is called to perform the necessary actions. Any *after.write* and *before.rewrite* sections in the UI script are ignored. So, if a UI script contains *after.write* and *after.rewrite* sections for the main table, you must replace these by *after.save.object()* hooks in the DAL.

## Arguments
| | | |
|---|---|---|
| `long` | `mode` |    |

## Return values
The hook returns 0 if successful. If the hook returns a negative value (DALHOOKERROR), the transaction should be canceled.
If the hook was called directly by the [4GL engine](../glossary/glossary.md#fourgl_engine), the transaction is canceled automatically. If the hook was not called by the [4GL engine](../glossary/glossary.md#fourgl_engine), the transaction must be canceled by calling [abort.transaction()](../functions_db_operations/abort.transaction.md) or [abort.io()](../functions_db_operations/abort.io.md), typically in the UI script.

## Context
This function is implemented in the 4GL Engine and can be used in DAL script types.

## Example
```

function extern long after.save.object(long mode)
{
    if mode = DAL_NEW then
        | this is code from after.write subsection
    else
        | this is code from after.rewrite subsection
    endif
}
```

## Related topics
- [Data Access Layer](overview.md)

- [DAL terminology](dal_glossary.md)

- [Object hooks](object_hooks.md)
