# enable.table.extension()

## Syntax:
`function void enable.table.extension( )`

## Description
This macro will enable the calling of ue hooks and table extension hooks. The actual state of the enabling as saved during [disable.table.extension()](disable.table.extension.md) will be used during enable.table.extension().

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  To prevent issues with non-working extensions, macros disable.table.extension() and enable.table.extension() must be coded together.
To help in the analysis of which table extension(s) might call a disable.table.extension() but not an enable.table.extension() a bshell trace with options
`-dbgfun -dbgflow -dbgcpu -tracelevel 3`
can be used and search on it for the words `DISABLE.UE.DLL` and `ENABLE.UE.DLL`.
There must be the same number of matches for `DISABLE.UE.DLL` as for `ENABLE.UE.DLL`. If this is not the case the calling function of the additional instruction could be identified in the trace having the options above.

## Example
```

function extern long ue.before.before.save.object(long mode)
{
        disable.table.extension()
        db.insert(...)	|Insert on the table of this ue dll
        enable.table.extension()
        return(0)
}
```

## Related topics
- [User Exit DLL Overview](overview.md)
- [Data Access Layer](../functions_dal/overview.md)
- [Object hooks](../functions_dal/object_hooks.md)
- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
