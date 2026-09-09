# standard.command.is.allowed()

## Syntax:
`function boolean standard.command.is.allowed( )`
`function boolean add.set.is.allowed( )`
`function boolean dupl.occur.is.allowed( )`
`function boolean modify.set.is.allowed( )`
`function boolean mark.delete.is.allowed( )`
`function boolean global.delete.is.allowed( )`
`function boolean text.manager.is.allowed( )`

## Description
You can use these hooks in your UI script to define the conditions under which the specific standard command should become enabled in the UI. The [4GL engine](../glossary/glossary.md#fourgl_engine) will use these hooks to determine whether the standard commands must be enabled or disabled.

## Return values
The hook should return TRUE in case the standard command is allowed. In that case the [4GL engine](../glossary/glossary.md#fourgl_engine) will enable the standard command on the UI. In any other case the hook should return FALSE.

## Context
This function is implemented in the 4GL Engine and can be used in all script types.

## When called
The [4GL engine](../glossary/glossary.md#fourgl_engine) will call one or more of these hooks just before the following event sections are executed:

- *before.display.object*

- Here commands are handled whose enabling depends on values of the whole occurrence. E.g. based on a status field the occurrence should be disabled and may not be deleted. For editable overview sessions the MODIFY.SET command is handled. For details session the MODIFY.SET, MARK.DELETE and TEXT.MANAGER commands are handled. (MODIFY.SET influences whether the whole occurrence will be disabled).

- *read.view* subevent of the *main.table.io* event

- Here commands are handled whose enabling depends on the current view. E.g. a closed order does not allow lines to be added, or deleted. The order number field can be in the view. For overview sessions the ADD.SET and GLOBAL.DELETE commands are handled. For details sessions the ADD.SET command is handled. For both types of sessions, the disabling of the DUPL.OCCUR command will be based the ADD.SET command, since DUPL.OCCUR is actually adding a record with default values.

- *after.choice* subevent of the *choice.mark.occur* event

- Here commands are handled whose enabling depends on whether records are marked. If one record is marked the DUPL.OCCUR, MARK.DELETE and TEXT.MANAGER commands are handled. DUPL.OCCUR is only handled in case the session has view fields, because the view may forbid lines to be added.

- The [4GL engine](../glossary/glossary.md#fourgl_engine) will also use the DAL [method.is.allowed()](../functions_dal/method.is.allowed.md) hook to determine whether the standard commands must be enabled or disabled:

- First, the UI hook will be called. If this returns FALSE, the command will be disabled, if it returns TRUE (or if it does not exist), the [method.is.allowed()](../functions_dal/method.is.allowed.md) hook will be called. If this returns FALSE, the command will be disabled, else it will be enabled.

- The disabling of the standard commands UPDATE.DB and RECOVER.SET is based on the command MODIFY.SET. This is because when the user is not allowed to modify data, the Save and Revert To Saved can also be disabled.

- As of TIV 1075 the standard command global.delete is no longer supported. See the [Improved Record selection Cookbook](../functions_selection/cookbook.md) for more information.

## Example
```

function extern boolean mark.delete.is.allowed()
{
    domain  fmfoc.oorg  origin.of.order

    fmfoc.dll0100.get.origin.of.order(fmfoc200.orno, origin.of.order)
    if origin.of.order <> fmfoc.oorg.man then
        return(false)
    endif

    return(true)
}
```

## Related topics
- [UI Template](overview.md)

- [form.command.is.allowed()](form.command.is.allowed.md)
