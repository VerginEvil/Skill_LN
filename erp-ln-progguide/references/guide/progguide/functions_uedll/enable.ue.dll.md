# enable.ue.dll()

## Syntax:
`function void enable.ue.dll( )`

## Description
This macro will enable the calling of ue hooks and table extension hooks. The actual state of the enabling as saved during disable.ue.dll will be used during enable.ue.dll.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## Example
```

function extern long ue.before.before.save.object(long mode)
{
        disable.ue.dll()
        db.insert(...)	|Insert on the table of this ue dll
        enable.ue.dll()
        return(0)
}
```

## Related topics
- [User Exit DLL Overview](overview.md)
- [Data Access Layer](../functions_dal/overview.md)
- [Object hooks](../functions_dal/object_hooks.md)
- [4GL main table i/o sections](../4gl_features/4gl_main_table_io_sections.md)
